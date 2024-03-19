from django import forms
from .models import Message






class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'message',)
        widgets = {
            'message': forms.Textarea(attrs={'rows':4}),
        }