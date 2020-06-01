from django.shortcuts import render
from .models import Creature
from django.views.generic import (
    ListView,
    DetailView
)


class HomeListView(ListView):
    model = Creature
    template_name = 'home/home.html'
    context_object_name = 'designs'
    ordering = ['category']
    paginate_by = 3


class AnimatedCreaturesListView(ListView):
    model = Creature
    template_name = 'graphics/creatures.html'
    context_object_name = 'designs'
    ordering = ['-date_made']
    paginate_by = 3
