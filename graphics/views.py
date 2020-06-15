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


class AnimatedCreaturesListView(ListView):
    model = Membership
    template_name ='graphics/creatures.html'


class AnimatedObjectsListView(ListView):
    model = Membership
    template_name ='graphics/objects.html'



class LandscapeListView(ListView):
    model = Membership
    template_name ='graphics/landscapes.html'
    


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
class OrderItemView(FormView):
    template_name = 'graphics/order_item.html'
    form_class = ItemOrderForm
    success_url = '/'

    def form_valid(self, form):
        send_mail('Order 2D Item',
                    'Thank you for your order! You will have get your order within 7 days.',
                    'hanzzanton@gmail.com',
                    ['anton.isak@outlook.com'],
                    fail_silently=False)
        
        return super().form_valid(form)


# """Send Requested Item"""
# def order_item(request):

#     if request.method == "POST":

#         form = ItemOrderForm(request.POST)
#         if form.is_valid():
#             send_mail('Order 2D Item',
#                 'Thank you for your order! You will have get your order within 7 days.',
#                 'hanzzanton@gmail.com',
#                 ['anton.isak@outlook.com'],
#                 fail_silently=False)
#             messages.success(request, f'Your request is being handled. An confirmation email has been sent to ')
#             return redirect('home')
#         else:
#             form = ItemOrderForm()
#         return render(request, 'graphics/order_item.html', {'form': form})
