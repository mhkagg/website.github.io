from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blogs, Profile, Search

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = {"first_name", "last_name", "username", "email", "password1", "password2"}

class MyForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = {"name","message"}

class SearchForm(forms.ModelForm):
    class Meta:
        model= Search
        fields= ['address',]

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


