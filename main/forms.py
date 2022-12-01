from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control my-2",'placeholder':"enter username"}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control my-2",'placeholder':"enter email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control my-2",'placeholder':"enter password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control my-2",'placeholder':"conform password"}))
    class Meta:
        model=User      
        fields=["email","username","password1",'password2']  
       
class TodoForm(forms.ModelForm):
    Start_Time=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control my-2",'type':"time"}))
    End_Time=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control my-2",'type':"time"}))
    class Meta:
        model=Todo
        fields=["title","Start_Time","End_Time","completed"]
  