from django.shortcuts import render
from .models import Agent
from property.models import Propertie,Category


def agents_grid(request):
    agent=Agent.objects.all()
    context = {
        "agent": agent
    }
    return render(request , 'agent/agents-grid.html' , context=context)

def agent_single(request,id):
    agent=Agent.objects.get(id=id)
    context={
        'agent':agent,
        'category': Category.objects.all(),
        'property': Propertie.objects.filter(status=True),  
    }
    return render(request , 'agent/agent-single.html' , context=context )
