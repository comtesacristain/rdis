from django.shortcuts import render

# Create your views here.
from data_manager.models import *
from boreholes.models import *


# Create your views here.
def index(request):
    duplicate_groups= DuplicateGroup.objects.all()
    return render(request, 'duplicates/index.html', {"duplicate_groups":duplicate_groups})
    #return HttpResponse("test")
	
def duplicate(request, id):
    duplicate_group= DuplicateGroup.objects.get(pk=id)
    duplicates = duplicate_group.duplicate_set.all() 
    enos = [x[0] for x in duplicates.values_list('table_id')]
    duplicate_entities=Entity.objects.filter(eno__in=enos)
    return render(request, 'duplicates/duplicate.html', {"duplicate_group":duplicate_group,"duplicates":duplicates})