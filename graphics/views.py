from django.shortcuts import render
from .models import Creature, Object, Landscape
from django.views.generic import (
    ListView,
    DetailView
)

"""Home ListViews (can make 1 single view for all 3? Checkout "Mixin")"""

# class HomeListViewCreature(ListView):
#     model = Creature
#     template_name = 'home/home.html'
#     context_object_name = 'creatures'
#     ordering = ['-date_made']
#     paginate_by = 1


# class HomeListViewObject(ListView):
#     model = Object
#     template_name = 'home/home.html'
#     context_object_name = 'objects'
#     ordering = ['-date_made']
#     paginate_by = 1


# class HomeListViewLandscape(ListView):
#     model = Landscape
#     template_name = 'home/home.html'
#     context_object_name = 'landscapes'
#     ordering = ['-date_made']
#     paginate_by = 1


#Change these 3 below "Mixin" 

"""Objects ListViews"""
class AnimatedCreaturesListView(ListView):
    model = Creature
    template_name = 'graphics/creatures.html'
    context_object_name = 'designs'
    ordering = ['-date_made']
    paginate_by = 3



class AnimatedObjectsListView(ListView):
    model = Object
    template_name = 'graphics/objects.html'
    context_object_name = 'designs'
    ordering = ['-date_made']
    paginate_by = 3



class LandscapeListView(ListView):
    model = Landscape
    template_name = 'graphics/landscapes.html'
    context_object_name = 'designs'
    ordering = ['-date_made']
    paginate_by = 3


"""Detail Views"""
class CreatureDetailView(DetailView):
    model = Creature


class ObjectDetailView(DetailView):
    model = Object


class LandscapeDetailView(DetailView):
    model = Landscape