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
        ]  # Include password fields
