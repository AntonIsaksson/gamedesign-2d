from django.shortcuts import render
from graphics.models import Designs

# def home(request):
#     context = {
#         'creatures': Creature.objects.all(),
#         'objects': Object.objects.all(),
#         'landscapes': Landscape.objects.all()
#     }
#     return render(request, 'home/home.html', context)


def home(request):
    context = {
        'designs': Designs.objects.all(),
    }
    return render(request, 'home/home.html', context)