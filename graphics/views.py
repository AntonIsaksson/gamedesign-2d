from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator 
from .forms import ItemOrderForm
from .models import Designs
from users.models import Membership, UserMembership
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


class AnimatedCreaturesListView(ListView):
    model = Membership
    template_name ='graphics/creatures.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
       
        return context


class AnimatedObjectsListView(ListView):
    model = Membership
    template_name ='graphics/objects.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
       
        return context



class LandscapeListView(ListView):
    model = Membership
    template_name ='graphics/landscapes.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
       
        return context


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
        else:
            context = {'object': None }
        return render(request, "graphics/detail.html", context)


# class CreatureDetailViewPremium(DetailView):
#     model = CreaturePremium
#     template_name = 'graphics/detail.html'


# class ObjectDetailView(DetailView):
    
#     def get(self, request, pk_free, *args, **kwargs):
        
#         creature = get_object_or_404(Object, pk=pk_free)
#         user_membership = get_object_or_404(UserMembership, user=request.user)
#         user_membership_type = user_membership.membership.membership_type
#         designs_allowed_mem_types = creature.allowed_memberships.all()
#         context = {'object': None }
#         if designs_allowed_mem_types.filter(membership_type=user_membership_type).exists():
#             context = {'object': creature }
#         else:
#             context = {'object': None }
#         return render(request, "graphics/detail.html", context)



# class LandscapeDetailView(DetailView):
#     def get(self, request, pk_free, *args, **kwargs):
        
#         creature = get_object_or_404(Landscape, pk=pk_free)
#         user_membership = get_object_or_404(UserMembership, user=request.user)
#         user_membership_type = user_membership.membership.membership_type
#         designs_allowed_mem_types = creature.allowed_memberships.all()
#         context = {'object': None }
#         if designs_allowed_mem_types.filter(membership_type=user_membership_type).exists():
#             context = {'object': creature }
#         else:
#             context = {'object': None }
#         return render(request, "graphics/detail.html", context)




"""Oreder Item FormView"""
class OrderItemView(FormView):
    template_name = 'graphics/order_item.html'
    form_class = ItemOrderForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# """Send Requested Item"""
# def order_item(request):

#     if request.method == "POST":

#         form = ItemOrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your request is being handled. An confirmation email has been sent to ')
#             return redirect('home')
#         else:
#             form = ItemOrderForm()
#         return render(request, 'graphics/order_item.html', {'form': form})
