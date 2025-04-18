from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import *
from .forms import *
import requests
import random

# .json() on a get request makes a usable python dict/list
# response = requests.get("http://www.omdbapi.com/?s=hangover&apikey=582a95e7")
# print(response.json()["Search"][0].get("Title"))


# home/landing route
@login_required(login_url="/login")
def home(request):
    action_movie_data = requests.get("http://www.omdbapi.com/?s=action&apikey=582a95e7")

    comedy_movie_data = requests.get("http://www.omdbapi.com/?s=comedy&apikey=582a95e7")

    scary_movie_data = requests.get("http://www.omdbapi.com/?s=scary&apikey=582a95e7")

    mystery_movie_data = requests.get(
        "http://www.omdbapi.com/?s=mystery&apikey=582a95e7"
    )

    # json() returns json as dict to send to template
    action_movie_data = action_movie_data.json().get("Search", [])

    comedy_movie_data = comedy_movie_data.json().get("Search", [])

    scary_movie_data = scary_movie_data.json().get("Search", [])

    mystery_movie_data = mystery_movie_data.json().get("Search", [])
    # gets search value which is a list or empty list default

    return render(
        request,
        "index.html",
        {
            "action_movie_data": action_movie_data,
            "comedy_movie_data": comedy_movie_data,
            "scary_movie_data": scary_movie_data,
            "mystery_movie_data": mystery_movie_data,
        },
    )


@login_required(login_url="/login")
def search(request):
    if request.method == "GET":
        input_value = request.GET.get("search-input")
        input_value = input_value.title()
        searched_movie_data = requests.get(
            f"http://www.omdbapi.com/?s={input_value}&apikey=582a95e7"
        )

        # json() returns json as dict to send to template
        searched_movie_data = searched_movie_data.json().get("Search", [])

    # we now pass the searched movie context
    return render(
        request,
        "search.html",
        {"searched_movie_data": searched_movie_data, "input_value": input_value},
    )


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.id)
            return redirect("home")

    return render(request, "login.html")


def logout_user(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.session.get("load_profile"):
                request.session.pop("load_profile")
            logout(request)
            return redirect("login")
    return redirect("login")


def signup(request):
    form = UserForm()

    return render(request, "sign-up.html", {"form": form})


# UserForm comes from our forms.py file
def create_account(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the new user
            return redirect("login")  # Redirect to login page after success

        return redirect("sign-up")


@login_required
def account_manage(request):
    form = PasswordChangeForm(user=request.user)
    return render(request, "account-manage.html", {form: "form"})


@login_required
def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("logout")
    print(form)
    return redirect("login")


def profiles(request):
    # If you want profiles per user:
    # user_profiles = Profiles.objects.filter(user=request.user)
    # If global profiles:
    user_profiles = Profiles.objects.all()
    max_profiles = 4

    if len(user_profiles) == 0 and request.session.get("load_profile"):
        request.session.pop("load_profile")

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid() and user_profiles.count() < max_profiles:
            profile = form.save(commit=False)
            # If per user:
            profile.user = request.user
            profile.save()
    else:
        form = ProfileForm()

    context = {
        "form": form,
        "profiles": user_profiles,
        "max_profiles": max_profiles,
    }
    return render(request, "profiles.html", context)


def load_profile(request):
    if request.method == "POST":
        # we are getting the value from name attribute in element
        if request.session.get("load_profile"):
            request.session["load_profile"] = request.POST.get("profile_id")
            return redirect("home")
        else:
            request.session["load_profile"] = request.POST.get("profile_id")
            return redirect("home")


def delete_profile(request):
    # query sets are sets of objects
    delete_profile = Profiles.objects.filter(id=request.POST.get("del_profile")).first()
    delete_profile.delete()
    if request.session.get("load_profile"):
        request.session.pop("load_profile")
    return redirect("profile")


"""Debugging functions to avoid excessive API calls 1,000k per day"""


# def login(request):
#     return render(request, "login.html")


# def search(request):
#     return render(request, "search.html")


# def home(request):
#     return render(request, "index.html")
