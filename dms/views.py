
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from forms import SignupForm, MessageForm, LoginForm


from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import MessageForm




def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')  # Redirect after successful form submission
    else:
        form = MessageForm()
    return render(request, 'dms/home.html', {'form': form})

            # save method pushes data into the backend 
            # Optionally, redirect to another page after successful form submission
            # return redirect('success_page')
    else:
        form = MessageForm()
    
    return render(request, 'dms/home.html', {'form': form})
def dashboard(request):
    return render(request,'dms/dashboard.html')


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to dashboard upon successful login
            else:
                # Handle invalid credentials here
                return render(request, 'dms/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'dms/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')  # Redirect to home page after logout

    return render(request,'dms/login.html')

def Try(request):
    return HttpResponse("hi")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to dashboard upon successful signup
    else:
        form = SignupForm()
    return render(request, 'dms/signup.html', {'form': form})