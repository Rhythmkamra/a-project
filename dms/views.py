from django.shortcuts import render
from .models import Document
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'index.html', {'documents': documents})
# Create your views here.
