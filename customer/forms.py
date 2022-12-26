from django import forms
from owner.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class": "form-control",'placeholder':'password'}))
    password2 = forms.CharField(label="confirm Password",widget=forms.PasswordInput(attrs={"class": "form-control",'placeholder':'confirm password'}))

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),

        }
       
        help_texts={
            'username':None
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class CartFrom(forms.Form):
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))


class CheckOutForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
