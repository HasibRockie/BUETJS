from django import forms
from django.forms import fields
from .models import Contact, Comment

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('commentor_name', 'commentor_email', 'comment')  
        # fields = '__all__'
        
