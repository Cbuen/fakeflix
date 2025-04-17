from django import forms
from .models import AuthUser, Profiles
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ModelForm


class searchForm(forms.Form):
    search_input = forms.CharField(max_length=100)


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ["profile"]

    # Explicitly set required if needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["profile"].required = True  # Ensures the field is required[4]


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


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Old password"}
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "new password"}
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
