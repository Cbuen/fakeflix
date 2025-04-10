from django import forms
from .models import AuthUser, Profiles


class searchForm(forms.Form):
    search_input = forms.CharField(max_length=100)


class UserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ["username", "first_name", "last_name", "email", "password"]
