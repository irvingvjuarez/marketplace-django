from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Ej. Jesse Pinkman",
        "class": "w-full p-2 outline-none rounded-xl"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Ej. email@example.com",
        "class": "w-full p-2 outline-none rounded-xl"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "w-full p-2 outline-none rounded-xl"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "w-full p-2 outline-none rounded-xl"
    }))