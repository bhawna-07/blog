from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth .models import User
from.models import BlogModel 

class SignUP(UserCreationForm):
    class Meta:
     model=User
     fields=['username','email']     
     
     



class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['author', 'title', 'message']
        labels = {
            'title': 'Blog title',
            'message': 'Write Your Blog Here:',
        }
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 10,
                'cols': 40,
                'placeholder': 'Start writing your blog...'
            }),
        }
