from django.shortcuts import render
from .models import Agent

def agents_grid(request):
    context = {
        "agent": Agent.objects.all()
    }
    return render(request , 'agent/agents-grid.html' , context=context)
def agent_single(request):
    return render(request , 'agent/agent-single.html' )
