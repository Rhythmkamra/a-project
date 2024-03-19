# models.py

from django.db import models
# from .workflows import message_workflow


    
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
