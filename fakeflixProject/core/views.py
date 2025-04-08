from django.shortcuts import render, redirect
import requests
import random

# .json() on a get request makes a usable python dict/list
# response = requests.get("http://www.omdbapi.com/?s=hangover&apikey=582a95e7")
# print(response.json()["Search"][0].get("Title"))


# home/landing route
def home(request):
    # get requests for movie data
    action_movie_data = requests.get("http://www.omdbapi.com/?s=action&apikey=582a95e7")

    comedy_movie_data = requests.get("http://www.omdbapi.com/?s=comedy&apikey=582a95e7")

    scary_movie_data = requests.get("http://www.omdbapi.com/?s=scary&apikey=582a95e7")

    mystery_movie_data = requests.get(
        "http://www.omdbapi.com/?s=mystery&apikey=582a95e7"
    )

    print(mystery_movie_data.json())

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


def search(request):
    return redirect('home')
