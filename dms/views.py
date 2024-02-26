from django.shortcuts import render,redirect
from .models import Document
from .forms import Signup

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'index.html', {'documents': documents})
# Create your views here.
def home(request):
    return render(request,'dms/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another URL after successful signup
            return redirect('success_url_name')  # Change 'success_url_name' to your actual URL name
    else:
        form = Signup()
    return render(request, 'dms/signup.html', {'form': form})


def dashboard(request):
    return render(request,'dms/dashboard.html')


def login(request):
    return render(request,'dms/login.html')


def about(request):
    return render(request,'dms/about.html')
