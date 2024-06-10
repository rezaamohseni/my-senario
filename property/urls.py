from django.urls import path
from django.contrib import admin
from .views import peroperty_single ,  property_grid
app_name = 'property'
urlpatterns = [
    path('' ,  property_grid , name = 'property-grid'),
    path('property-grid/<str:category> ',  property_grid , name = 'list_by_category'),
    path('property-single/<int:id>' , peroperty_single , name='property-single'),
    path('property-single/<int:id>' , peroperty_single , name='property-single'),
]