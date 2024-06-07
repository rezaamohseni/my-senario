from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path('', home, name='root' ),
    path('contact/', contact , name='root'),
    path('about/', about , name='root'),
]
