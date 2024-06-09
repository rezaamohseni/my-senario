from django.shortcuts import render
from .models import Propertie , Category
from django.core.paginator import Paginator,EmptyPage , PageNotAnInteger

def property_grid(request,**kwargs):
    if kwargs.get('category'):
        all_service = Propertie.objects.filter(category__title=kwargs.get('category'))
    
    else:
        all_service = Propertie.objects.filter(status=True)
    all_services = Paginator(all_service,1) 
    last_page = all_services.num_pages
      
    try:
        page_number = request.GET.get('page')
        all_services = all_services.get_page(page_number)
    except PageNotAnInteger:
        all_services = all_services.get_page(1)
    except EmptyPage:
        all_services = all_services.get_page(1)
    context = {
        'property' : all_services,
        'category' : Category.objects.all()
    }
    return render(request , 'property/property-grid.html', context=context)
def peroperty_single(request , id):
    
    return render(request , 'property/property-single.html' )
