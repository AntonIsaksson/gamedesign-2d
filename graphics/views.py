from django.shortcuts import render
from .models import GraphicDesigns


def all_graphics(request):
    context = {
        'designs': GraphicDesigns.objects.all()
    }
    return render(request, 'graphics/graphics.html', context)


