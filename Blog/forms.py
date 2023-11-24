from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth  import password_validation
from django import forms
from .models import Post, Profile
class RegisterForm(UserCreationForm):
    username = forms.CharField (label = ('Username:'), 
                               widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField (label = ('first name:'), 
                               widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    
    email=forms.EmailField (max_length=64, help_text='Enter a valid email address' ,
                            widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    password1=forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                              help_text=password_validation.password_validators_help_text_html())
    
    password2=forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}),
                              help_text=('Just Enter the same password, for confirmation'))

    class Meta:
        model = User #to use the defualt database provided by django
        fields = ['username', 'email','password1','password2']


class ImageForm(forms.ModelForm):
    post_img = forms.ImageField(
        label='Add Cover Image',
        widget=forms.ClearableFileInput(
            attrs={'class':'form-control','name':'image','type':'file','id':'formFile'}))
    class Meta:
        model = Post
        fields  = ['post_img']



