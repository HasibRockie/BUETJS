from django import forms
from django.forms import fields
from .models import Contact, AllComment, Viewer, Gellery,Post
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta():
        model = AllComment
        fields = ('comment',)  
        #fields = '__all__'

class GellaryForm(forms.ModelForm):
    class Meta():
        model = Gellery 
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta():
        model = Post 
        fields = '__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ["first_name","last_name","is_superuser","username","email","password1","password2"] 

class ViewerForm(forms.ModelForm):
    class Meta:
        model = Viewer
        fields = '__all__'
        exclude = ['user']