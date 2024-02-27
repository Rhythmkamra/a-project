# models.py

from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    remarks = models.TextField(blank=True)


    def __str__(self):
        return self.title

# Create your models here.
