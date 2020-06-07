from django.shortcuts import render
from graphics.models import Creature, Object, Landscape

# def home(request):
#     context = {
#         'creatures': Creature.objects.all(),
#         'objects': Object.objects.all(),
#         'landscapes': Landscape.objects.all()
#     }
#     return render(request, 'home/home.html', context)

def home(request):
    creatures = Creature.objects.all()
    objects = Object.objects.all()
    landscapes = Landscape.objects.all()
    return render(request, 'home/home.html', {'creatures': creatures, 'objects': objects, 'landscapes': landscapes})