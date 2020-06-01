from django.shortcuts import render
from graphics.models import Creature

def home(request):
    context = {
        'designs': DesignType.objects.all()
    }
    return render(request, 'home/home.html', context)

