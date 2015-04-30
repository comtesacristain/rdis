from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from data_manager.models import *
from boreholes.models import *


# Create your views here.
def index(request):
    duplicate_groups= DuplicateGroup.objects.order_by('-num_dupes').all()
    paginator = Paginator(duplicate_groups, 20)
    page = request.GET.get('page')
    try:
        dg = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dg = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dg = paginator.page(paginator.num_pages)
		
    return render(request, 'duplicates/index.html', {"duplicate_groups":dg})
    #return HttpResponse("test")
	
def duplicate(request, id):
    duplicate_group= DuplicateGroup.objects.get(pk=id)
    duplicates = duplicate_group.duplicate_set.all() 
    enos = [x[0] for x in duplicates.values_list('eno')]
    duplicate_entities=Entity.objects.filter(eno__in=enos)
    return render(request, 'duplicates/duplicate.html', {"duplicate_group":duplicate_group,"duplicate_entities":duplicates})