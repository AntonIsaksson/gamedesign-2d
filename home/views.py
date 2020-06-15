from django.shortcuts import render
from graphics.models import Designs
from users.models import Membership, UserMembership
from django.views.generic import ListView




class HomeListView(ListView):
    model = Designs
    template_name ='home/home.html'
    
