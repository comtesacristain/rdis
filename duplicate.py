from boreholes.models import Borehole
from django.contrib.gis.measure import D
from data_manager.models import *
exact_locations = list()
boreholes = Borehole.objects.all()
for borehole in boreholes:
    if borehole.geom:
        if borehole.geom.z is None:
            print borehole.eno
            dups = Borehole.objects.filter(geom__equals=borehole.geom)
            if len(dups) > 1:
                exact_locations.append(dups)
                
for exact_location in exact_locations:
    enos = list(exact_location.values_list("eno",flat=True))
    dd = Duplicate.objects.filter(table_id__in=enos).values_list("table_id",flat=True)
    if set(enos).difference(dd):
        dt = DuplicateType(kind="EXACT",field="GEOM",model="DRILLHOLE")
        dt.save()
    for e in set(enos).difference(dd):
        d=Duplicate(table_id=e,table_name="entities",duplicate=dt)
        d.save()