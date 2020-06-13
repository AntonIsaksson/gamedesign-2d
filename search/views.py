from django.shortcuts import render
from django.db.models import Q, CharField
from graphics.models import CreatureFree, CreaturePremium, ObjectFree, ObjectPremium, LandscapeFree, LandscapePremium
from django.db.models.functions import Lower

# def do_search(request):
#     CharField.register_lookup(Lower, "lower")
#     designs = CreatureFree.objects.filter(title__lower__contains=request.GET['q'])
#     return render(request, "graphics/creatures.html", {'designs': designs})

def do_search(request):
    CharField.register_lookup(Lower, "lower")

    freedesigns = CreatureFree.objects.filter(title__lower__contains=request.GET['q'])
    premiumdesigns = CreaturePremium.objects.filter(title__lower__contains=request.GET['q'])
    freeobjects = ObjectFree.objects.filter(title__lower__contains=request.GET['q'])
    premiumobjects = ObjectPremium.objects.filter(title__lower__contains=request.GET['q'])
    freelandscapes = LandscapeFree.objects.filter(title__lower__contains=request.GET['q'])
    premiumlandscapes = LandscapePremium.objects.filter(title__lower__contains=request.GET['q'])



    
    return render(request, "graphics/search.html", {'freedesigns':freedesigns, 'premiumdesigns':premiumdesigns, 
                                                    'freeobjects':freeobjects, 'premiumobjects':premiumobjects,
                                                    'freelandscapes':freelandscapes, 'premiumlandscapes':premiumlandscapes })
