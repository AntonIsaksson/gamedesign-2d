from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator 
from .forms import ItemOrderForm
from .models import Designs
from users.models import Membership, UserMembership
from django.core.mail import send_mail
from django.views.generic import (
    View,
    ListView,
    DetailView,
)
from django.views.generic.edit import FormView


def get_user_membership(request):
        user_membership_qs = UserMembership.objects.filter(user=request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first()
        return None


class LatestItemsListView(ListView):
    model = Designs
    template_name = 'graphics/latest.html'
    ordering = ['-date_made']
    paginate_by = 6


class AnimatedCreaturesListView(ListView):
    model = Membership
    template_name ='graphics/creatures.html'

class AllCreaturesListView(ListView):
    model = Membership
    template_name ='graphics/all_creatures.html'
    ordering = ['-id']


class AnimatedObjectsListView(ListView):
    model = Membership
    template_name ='graphics/objects.html'

class AllObjectsListView(ListView):
    model = Membership
    template_name ='graphics/all_objects.html'
    ordering = ['-id']



class LandscapeListView(ListView):
    model = Membership
    template_name ='graphics/landscapes.html'
    
class AllLandscapesListView(ListView):
    model = Membership
    template_name ='graphics/all_landscapes.html'
    ordering = ['-id']


"""Detail Views"""
class DetailView(LoginRequiredMixin, DetailView):
    
    def get(self, request, pk_free, *args, **kwargs):
        
        creature = get_object_or_404(Designs, pk=pk_free)
        user_membership = get_object_or_404(UserMembership, user=request.user)
        user_membership_type = user_membership.membership.membership_type
        designs_allowed_mem_types = creature.allowed_memberships.all()
        context = {'object': None }
        if designs_allowed_mem_types.filter(membership_type=user_membership_type).exists():
            context = {'object': creature }
        elif designs_allowed_mem_types.filter(membership_type='Free').exists(): 
            context = {'object': creature }
        else:
            context = {'object': None }
        return render(request, "graphics/detail.html", context)



"""Order Item FormView"""
class OrderItemView(LoginRequiredMixin, FormView):
    template_name = 'graphics/order_item.html'
    form_class = ItemOrderForm
    success_url = '/'

    def form_valid(self, form):
        send_mail('Order 2D Item',
                    'Thank you for your order! We will get back to you within 3 working days with a paymentplan.',
                    'hanzzanton@gmail.com',
                    ['anton.isak@outlook.com'],
                    fail_silently=False)
        
        return super().form_valid(form)

