from django.shortcuts import render

def property_grid(request):
    return render(request , 'property/property-grid.html' )
def peroperty_single(request):
    return render(request , 'property/property-single.html' )
