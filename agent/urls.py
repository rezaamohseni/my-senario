from django.urls import path
from django.contrib import admin
from .views import agent_single , agents_grid
from property.views import peroperty_single , property_grid
app_name = 'agent'
urlpatterns = [
    path('' , agents_grid , name = 'agent-grid'),
    path('agent-single/<int:id>' , agent_single , name='agent-single'),
    path('agent-single/<int:id>' , agent_single , name='agent-single'),
    path('property/<str:category>' , property_grid, name='list_by_category'),
    path('property-single/<int:id>' , peroperty_single , name='list_by_single'),
    
]