from django.forms import ModelForm
from django import forms
from .models import blog
from django.contrib.auth.models import User

class BlogsForm(ModelForm):
    class Meta:
        model = blog
        fields = ['Title','description','type']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-select'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }
        
        
class UserForm(ModelForm):
    class meta:
        model = User
        fields = ['username','password']
        widgets= {
            'username':forms.TextInput(attrs={'class:from-control mt-3'}),
            'password': forms.PasswordInput(attrs={'class:from-select mt-3'})
        }
        labels = {
            'username' : ('username:')
        }
        help_texts = {
            'username':(),
        }