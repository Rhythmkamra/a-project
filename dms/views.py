from django.shortcuts import render,redirect
from .models import Document
from .forms import Signup
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import MessageForm



def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add further processing here if needed
        else:
            # If the form is not valid, it will render with the entered data and error messages
            return render(request, 'home.html', {'form': form})
    else:
        form = MessageForm()
    return render(request, 'home.html', {'form': form})

def dashboard(request):
    return render(request,'dms/dashboard.html')


def login(request):
    return render(request,'dms/login.html')



