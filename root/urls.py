from django.urls import path
from django.contrib import admin
from .views import home , contact , about
app_name = 'root'
urlpatterns = [
    path('' , home , name = 'home'),
    path('about/' , about , name='about'),
    path('contact/' , contact , name='contact'),
]
