from django.shortcuts import render
from django.db.models import Q, CharField
from graphics.models import Creature
from django.db.models.functions import Lower

def do_search(request):
    CharField.register_lookup(Lower, "lower")
    designs = Creature.objects.filter(title__lower__contains=request.GET['q'])
    return render(request, "graphics/creatures.html", {'designs': designs})

