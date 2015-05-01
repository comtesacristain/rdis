from django.core.management.base import BaseCommand, CommandError
from data_manager.models import Duplicate, DuplicateGroup
from rdis import database
from collections import Counter
import cx_Oracle,re

exact = "select eno, entityid, geom, entity_type from a.entities e where sdo_equal(e.geom,{geom})='TRUE' and entity_type in ('DRILLHOLE','WELL') and eno <> {eno}"
hundred_metres = "select eno, entityid, geom, entity_type from a.entities e where sdo_within_distance(e.geom,{geom},'distance= 100,units=m')='TRUE' and entity_type in ('DRILLHOLE','WELL') and eno <> {eno}"
ten_metres = "select eno, geom, entity_type from a.entities e where sdo_within_distance(e.geom,{geom},'distance= 10,units=m')='TRUE' and entity_type in ('DRILLHOLE','WELL') and eno <> {eno}"

#spatial_queries ={"exact":exact,"hundred_metres":hundred_metres,"ten_metres":ten_metres}
spatial_queries ={"exact":exact,"hundred_metres":hundred_metres}

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    exact = "select eno, entityid, geom, entity_type from a.entities e where sdo_equal(e.geom,{geom})='TRUE' and entity_type in ('DRILLHOLE','WELL') and eno <> {eno}"
    hundred_metres = "select eno, entityid, geom, entity_type from a.entities e where sdo_within_distance(e.geom,{geom},'distance= 100,units=m')='TRUE' and entity_type in ('DRILLHOLE','WELL') and eno <> {eno}"
    ten_metres = "select eno, geom, entity_type from a.entities e where sdo_within_distance(e.geom,{geom},'distance= 10,units=m')='TRUE' and entity_type in ('DRILLHOLE','WELL') and eno <> {eno}"

    #spatial_queries ={"exact":exact,"hundred_metres":hundred_metres,"ten_metres":ten_metres}
    spatial_queries ={"exact":exact,"hundred_metres":hundred_metres}
    
    def add_arguments(self, parser):
        parser.add_argument('mode', type=str)
        
    def handle(self, *args, **options):
        mode= options['mode']
        if mode == 'find_duplicates':
            self.find_duplicates()
        elif mode == 'rank_duplicates':
            self.rank_duplicates()
    
    def find_duplicates(self):
        
        conn=cx_Oracle.connect(database.DATABASES['production']['USER'],database.DATABASES['production']['PASSWORD'],database.DATABASES['production']['NAME'])
        curs=conn.cursor()
        curs.execute("alter session set nls_date_format='DD-MON-YYYY'")
        entities=curs.execute("select eno, entityid, geom, entity_type from a.entities where entity_type in ('DRILLHOLE', 'WELL') and geom is not null").fetchall()
        #duplicates = list()
        for entity in entities:
            for key in spatial_queries.keys():
                geom = entity[2]
                if geom is not None:
                    search_geometry = self.to_sdo_string(geom)
                    stmt = spatial_queries[key].format(eno=entity[0],geom=search_geometry)
                    results=curs.execute(stmt).fetchall()
                    if results.__len__() > 0:
                        self.insert_dupes(entity, results,key)
    
    def insert_dupes(self,orig,dupe_set,kind):
        dupe_groups = DuplicateGroup.objects.filter(duplicate__eno=orig[0],kind=kind)
        if dupe_groups.exists():
            dupe_group=dupe_groups.first()
        else:
            dupe_group = DuplicateGroup(kind=kind,field="GEOM")
            dupe_group.save()
            duplicate=Duplicate(eno=orig[0],entityid=orig[1],x=orig[2].SDO_POINT.X, y=orig[2].SDO_POINT.Y, z=orig[2].SDO_POINT.Z,table_name="entities",duplicate_group=dupe_group,entity_type=orig[3])
            duplicate.save()
        for dupe in dupe_set:
            duplicates = dupe_group.duplicate_set.filter(eno=dupe[0])
            if duplicates.exists():
                duplicate=duplicates.first()
            else:
                duplicate = Duplicate(eno=dupe[0],entityid=dupe[1],x=dupe[2].SDO_POINT.X, y=dupe[2].SDO_POINT.Y, z=dupe[2].SDO_POINT.Z, table_name="entities",duplicate_group=dupe_group,entity_type=dupe[3])
                duplicate.save()
        dupe_group.num_dupes = dupe_group.duplicate_set.count()
        dupe_group.save()

    def to_sdo_string(self,geom):
        if geom is None:
            return "NULL"
        if geom.type.__str__() == '<cx_Oracle.ObjectType MDSYS.SDO_GEOMETRY>':
            gtype = geom.SDO_GTYPE.__int__()
            point = self.to_sdo_string(geom.SDO_POINT)
            srid = geom.SDO_SRID.__int__()
            element_info = self.to_sdo_string(geom.SDO_ELEM_INFO)
            ordinates = self.to_sdo_string(geom.SDO_ORDINATES)
            return 'SDO_GEOMETRY({0},{1},{2},{3},{4})'.format(gtype,srid,point,element_info,ordinates)
        if geom.type.__str__() == '<cx_Oracle.ObjectType MDSYS.SDO_POINT_TYPE>':
            if geom.Z is None:
                return "SDO_POINT_TYPE({0},{1},NULL)".format(geom.X,geom.Y)
            else:
                return "SDO_POINT_TYPE({0},{1},{2})".format(geom.X,geom.Y,geom.Z)
                
    def rank_duplicates(self):
        dupe_groups = DuplicateGroup.objects.all()
        for duplicate_group in dupe_groups:
            print duplicate_group.id
            duplicates = duplicate_group.duplicate_set
            type_set = list(set(duplicates.values_list('entity_type',flat=True)))
            if len(type_set) == 2:
                self.rank_well_and_drillhole(duplicates)
            elif type_set[0] == 'WELL':
                self.rank_wells(duplicates)
            elif type_set[0] == 'DRILLHOLE':
                self.rank_drillholes(duplicates)
            #duplicates = duplicate_group.duplicate_set.all()
            #self.rank(duplicates)
            actions = duplicate_group.duplicate_set.values_list("action_status",flat=True)
            if "DELETE" in actions:
                duplicate_group.has_resolution = 'Y'
                duplicate_group.save()
    
    def rank_well_and_drillhole(self, duplicates):
        well_set=duplicates.filter(entity_type='WELL')
        drillhole_set = duplicates.filter(entity_type='DRILLHOLE')
        if len(well_set) == 1:
            well = well_set.first()
            well.action_status='KEEP'
        else:
            self.rank_wells(well_set)
            return
        drillhole_names=drillhole_set.values_list('entityid',flat=True)
        if self.parse_string(well.entityid) in [self.parse_string(name) for name in drillhole_names]:
            drillhole_set.filter(entityid__iregex=self.regex_string(well.entityid)).update(action_status='DELETE',data_transferred_to=well.eno)
        else: 
            pass    
        well.save()

        

    
    
    def rank_wells(self,duplicates):
        pass
    
    def rank_drillholes(self, duplicates):
        names = self.name_dictionary(duplicates.values_list('entityid',flat=True))
        
        if len(names) > 1:
            for n in names:
                if len(names[n]) > 1:
                    self.rank_drillholes(duplicates.filter(entityid__in=names[n]))
        elif len(names) == 1:
            print duplicates.values_list("z",flat=True)
            dates = dict([(duplicate.entity().entrydate,duplicate.eno) for duplicate in duplicates.all()])
            eno = dates[min(dates.keys())]
            duplicates.filter(eno=eno).update(action_status='KEEP')
            duplicates.exclude(eno=eno).update(action_status='DELETE',data_transferred_to=eno)
        pass
    
    def name_dictionary(self,names):
        d =dict()
        names=zip([self.strip_leading_zeros(name) for name in names], names)
        for key, val in names:
            d.setdefault(key, []).append(val)
        return d    
   
    def strip_leading_zeros(self, s):
        return re.sub('(?<=[A-Z])+0+','',s)
    
    def parse_string(self, s):
        s=s.lower()
        return re.sub('[\W_]+', ' ', s)
        
    def regex_string(self, s):
        return re.sub('[\W_]+','.',s)
