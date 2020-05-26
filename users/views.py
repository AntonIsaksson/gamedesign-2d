from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('/')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})
