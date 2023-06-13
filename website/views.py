from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def home(request):
    # check if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)

        # login user
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in. Please try again.')
            return redirect('home')
        
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    pass