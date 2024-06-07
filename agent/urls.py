from django.urls import path
from django.contrib import admin
from .views import agent_single , agents_grid
app_name = 'agent'
urlpatterns = [
    path('' , agents_grid , name = 'agent-grid'),
    path('agent-single/' , agent_single , name='agent-single'),
]