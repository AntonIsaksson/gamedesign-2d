from django.shortcuts import render
from .forms import UserRegistrationForm

def registration(request):
    form = UserRegistrationForm
    return render(request, 'users/registration.html', {'form': form})
