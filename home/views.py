from django.shortcuts import render
from graphics.models import CreatureFree, CreaturePremium, ObjectFree, ObjectPremium, LandscapeFree, LandscapePremium

# def home(request):
#     context = {
#         'creatures': Creature.objects.all(),
#         'objects': Object.objects.all(),
#         'landscapes': Landscape.objects.all()
#     }
#     return render(request, 'home/home.html', context)


def home(request):
    context = {
        'creaturesf': CreatureFree.objects.all(),
        'creaturesp': CreaturePremium.objects.all(),
        'objectsf': ObjectFree.objects.all(),
        'objectsp': ObjectPremium.objects.all(),
        'landscapesf': LandscapeFree.objects.all(),
        'landscapesp': LandscapePremium.objects.all()
    }
    return render(request, 'home/home.html', context)