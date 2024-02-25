from django.db import models

class Document(models.Model):
    remarks = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.document.name


# Create your models here.
