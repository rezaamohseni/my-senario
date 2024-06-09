from django.shortcuts import render
from property.models import Propertie
from .models import Service , Testimonial
from agent.models import Agent
from blog.models import Blog

def home(request):
    context = {
        'property' : Propertie.objects.filter(status=True)[:3],
        'home' : Service.objects.filter(status=True),
        'testimonials' : Testimonial.objects.all(),
        'agent' : Agent.objects.all(),
        'news' : Blog.objects.filter(status=True)
        
    }
    return render(request , 'root/index.html' , context=context)
def about(request):
    context={
        'agent' : Agent.objects.all()
    }
    return render(request , 'root/about.html', context=context )
def contact(request):
    return render(request , 'root/contact.html' )

