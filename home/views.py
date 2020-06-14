from django.shortcuts import render
from graphics.models import Designs
from users.models import Membership, UserMembership
from django.views.generic import ListView


# def home(request):
#     context = {
#         'designs': Designs.objects.all(),
#     }
#     return render(request, 'home/home.html', context)


def get_user_membership(request):
        user_membership_qs = UserMembership.objects.filter(user=request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first()
        return None


class HomeListView(ListView):
    model = Membership
    template_name ='home/home.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
       
        return context