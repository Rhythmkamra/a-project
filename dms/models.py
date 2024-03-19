# models.py
import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'armyproject.settings')

# Configure Django
django.setup()

# Now you can import your models and work with them

# Your code here


from django.db import models
# from .workflows import message_workflow




    def __str__(self):
        return self.title


    
from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    # remarks = models.FileField(upload_to='remarks/')
    created_at = models.DateTimeField(auto_now_add=True)
    # workflow = models.ForeignKey(message_workflow, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

        # Create your models here.