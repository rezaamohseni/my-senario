from django.urls import path
from django.contrib import admin
from .views import home , contact , about
from property.views import peroperty_single 
from agent.views import agent_single
from blog.views import blog_single
app_name = 'root'
urlpatterns = [
    path('' , home , name = 'home'),
    path('about/' , about , name='about'),
    path('contact/' , contact , name='contact'),
    path('new/<int:id>' , blog_single , name='list_by_blog'),
    path('person/<int:id>' , peroperty_single , name='list_by_property'),
    path('person/<int:id>' , agent_single , name='list_by_person'),
    
]
