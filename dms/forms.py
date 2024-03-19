import os
from django import forms


# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "armyproject.settings")
import django
django.setup()
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message  # Use absolute import
class Signup(UserCreationForm):
 password1 = forms.CharField(label ='Password',widget=forms.PasswordInput)
 password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username','first_name','last_name','email']

from .models import Message



class Login(UserCreationForm):
 username = forms.CharField(label ='Username',widget=forms.TextInput)
 password = forms.CharField(label='Password',widget=forms.PasswordInput)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'message',)
        widgets = {
            'message': forms.Textarea(attrs={'rows':4}),
        }