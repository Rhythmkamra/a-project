from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message

class Signup(UserCreationForm):
 password1 = forms.CharField(label ='Password',widget=forms.PasswordInput)
 password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username','first_name','last_name','email']
  labels ={'firs_name':'First_name','last_name':'Last_name','email':'Email'}




class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'message', 'remarks')
        widgets = {
            'message': forms.Textarea(attrs={'rows':4}),
        }