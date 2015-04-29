from django.core.management.base import BaseCommand, CommandError
from data_manager.models import Duplicate, DuplicateGroup
from rdis import database
import cx_Oracle,csv

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
                        #duplicates.append(results)
                        print entity
                        print results
                        print key
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
            duplicates = duplicate_group.duplicate_set.all()
            self.rank(duplicates)
    
    def rank(self, duplicates):
        duplicate = duplicates.first()
        remaining_set = duplicates.exclude(id=duplicate.id)
        if duplicate.entity_type == 'WELL':
            print duplicate
            remaining_well_set=remaining_set.filter(entity_type='WELL')
            if not remaining_well_set.exists():
                duplicate.deletion_status='KEEP'
            elif remaining_well_set.filter(entityid__ieq=duplicate.entityid):
                duplicate.deletion_status='UN'
        elif duplicate.entity_type == 'DRILLHOLE':
            remaining_well_set=remaining_set.filter(entity_type='WELL')
            if remaining_well_set.exists():
                duplicate.deletion_status='DELETE'
        duplicate.save()
        if remaining_set.exists():
            self.rank(remaining_set)
            # for duplicate in duplicate_group.duplicate_set.all():
                # if duplicate.entity_type =='WELL':
                    # remaining_set = duplicate_group.duplicate_set.exclude(id=duplicate.id).filter(entity_type="WELL")
                    # if remaining_set.filter(entity_type="WELL").exists():
                        # print remaining_set
                    # else:
                        # print "DUPLICATE SCORE UP"
                # elif duplicate.entity_type =='DRILLHOLE':
                    # print "DUPLICATE SCORE DOWN"
    
    def check_for_wells(self, remaining_set):
        remaining_set
 