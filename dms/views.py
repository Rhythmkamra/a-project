from django.shortcuts import render,redirect
from .models import Document
from .forms import Signup
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import MessageForm

def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MessageForm()
    return render(request, 'home.html', {'form': form})

class DraftDocumentView(CreateView):
    model = Document
    fields = ['title', 'file', 'remarks']
    template_name = 'draft_document.html'
    success_url = '/review/'

    def form_valid(self, form):
        form.instance.workflow_state = 'draft'  # Update workflow state
        return super().form_valid(form)

class ReviewDocumentView(DetailView):
    model = Document
    template_name = 'review_document.html'

class ApproveDocumentView(UpdateView):
    model = Document
    fields = ['remarks']
    template_name = 'approve_document.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.workflow_state = 'approved'  # Update workflow state
        return super().form_valid(form)

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'index.html', {'documents': documents})
# Create your views here.



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



