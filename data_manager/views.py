from django.shortcuts import render

# Create your views here.
from data_manager.models import *

# Create your views here.
def index(request):
    duplicate_groups= DuplicateGroup.objects.all()
    return render(request, 'duplicates/index.html', {"duplicate_groups":duplicate_groups})
    #return HttpResponse("test")
	
def duplicate(request, id):
    duplicate_group= DuplicateGroup.objects.get(pk=id)
    duplicates = duplicate_group.duplicate_set.all() 
    return render(request, 'duplicates/duplicate.html', {"duplicate_group":duplicate_group,"duplicates":duplicates})