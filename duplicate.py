from boreholes.models import Borehole
exact_locations = list()
boreholes = Borehole.objects.all()
for borehole in boreholes:
    if borehole.geom:
        if borehole.geom.z is None:
            print borehole.eno
            dups = Borehole.objects.filter(geom__equals=borehole.geom)
            if len(dups) > 1:
                exact_locations.append(dups)