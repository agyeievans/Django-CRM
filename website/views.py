from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    # fetching all records
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records':records})

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
    
# single customer record
def customer_record(request, pk):
    # check if user is logged in
    if request.user.is_authenticated:
        # Look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view page")
        return redirect('home')

# delete customer record
@login_required(login_url="home")
def delete_record(request, pk):
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Customer record deleted successfully....")
    return redirect('home')
    
# add record
@login_required(login_url="home")
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Customer record added successfully....")
                return redirect('home')

        return render(request, 'add_record.html', {'form':form})
    else:
       messages.success(request, "You must be logged in....")
       return redirect('home')




    
    
