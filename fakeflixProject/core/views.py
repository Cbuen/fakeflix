from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
import requests
import random

# .json() on a get request makes a usable python dict/list
# response = requests.get("http://www.omdbapi.com/?s=hangover&apikey=582a95e7")
# print(response.json()["Search"][0].get("Title"))


# home/landing route
@login_required(login_url="/login")
def home(request):
    # get requests for movie data
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


def login(request):
    if request.method == "POST":
        print(request.POST.get("username"))

    return render(request, "login.html")

def signup(request):
    return render(request, "sign-up.html")

# UserForm comes from our forms.py file
# simply .save() and call the request on the from to see if valid
def create_account(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")    
    return redirect("signup")


"""Debugging functions to avoid excessive API calls 1,000k per day"""


# def login(request):
#     return render(request, "login.html")


# def search(request):
#     return render(request, "search.html")


# def home(request):
#     return render(request, "index.html")
