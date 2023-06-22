from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email=forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user            
       
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        exclude=['user',]
  