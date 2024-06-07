from django.urls import path
from django.contrib import admin
from .views import peroperty_single ,  property_grid
app_name = 'property'
urlpatterns = [
    path('' ,  property_grid , name = 'property-grid'),
    path('property-single/' , peroperty_single , name='property-single'),
]