from django.shortcuts import render
import requests
import json

# .json() on a get request makes a usable python dict/list
# response = requests.get("http://www.omdbapi.com/?s=hangover&apikey=582a95e7")
# print(response.json()["Search"][0].get("Title"))


# Create your views here.
def home(request):
    action_movie_data = requests.get("http://www.omdbapi.com/?s=action&apikey=582a95e7")

    comedy_movie_data = requests.get("http://www.omdbapi.com/?s=comedy&apikey=582a95e7")

    scary_movie_data = requests.get("http://www.omdbapi.com/?s=scary&apikey=582a95e7")

    action_movie_data = action_movie_data.json().get("Search", [])

    comedy_movie_data = comedy_movie_data.json().get("Search", [])

    scary_movie_data = scary_movie_data.json().get("Search", [])

    return render(
        request,
        "index.html",
        {
            "action_movie_data": action_movie_data,
            "comedy_movie_data": comedy_movie_data,
            "scary_movie_data": scary_movie_data,
        },
    )
