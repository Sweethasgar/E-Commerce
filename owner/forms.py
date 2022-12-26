from django import forms
from owner.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderUpdateForm(forms.Form):
    options = (

        ("dispatched", "dispatched"),
        ("in-transit", "in-transit"),

    )
    status = forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-select"}))
    expected_delivery_date = forms.DateTimeField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
