from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm

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

# logout user
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

# register user
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered your account")
            return redirect('home')
    
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})
    

