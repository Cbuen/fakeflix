from django import forms
from .models import AuthUser, Profiles
from django.contrib.auth.forms import UserCreationForm


class searchForm(forms.Form):
    search_input = forms.CharField(max_length=100)


class UserForm(UserCreationForm):
    class Meta:
        model = AuthUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter your username"}),
            "first_name": forms.TextInput(
                attrs={"placeholder": "Enter your first name"}
            ),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
            "password1": forms.PasswordInput(
                attrs={"placeholder": "Create a password"}
            ),
            "password2": forms.PasswordInput(
                attrs={"placeholder": "Confirm your password"}
            ),
        }
