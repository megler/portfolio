from json import load
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from dotenv import load_dotenv
from movies.models import Movie
from movies.forms import Movie_Title, Movie_Rating
import os, requests, json

load_dotenv()

MDB_API_KEY = os.environ.get("MDB_API_KEY")


def index(request):

    all_movies = Movie.objects.filter().order_by("rating")
    return render(request, "movies/index.html", {"movies": all_movies})


def add(request):
    if request.POST:
        add_movie_form = Movie_Title(request.POST)
        if add_movie_form.is_valid():
            movie_title = add_movie_form.cleaned_data["movie_title"]
            return HttpResponseRedirect(
                reverse("movies:select", kwargs={"title": movie_title}))
    else:
        add_movie_form = Movie_Title()

    return render(request, "movies/add.html", {"form": add_movie_form})


def edit(request, id):
    movie_to_update = Movie.objects.get(pk=id)
    if request.POST:
        update_form = Movie_Rating(request.POST)
        if update_form.is_valid():
            movie_rating = update_form.cleaned_data["movie_rating"]
            movie_review = update_form.cleaned_data["movie_review"]
            movie_to_update.rating = movie_rating
            movie_to_update.review = movie_review
            movie_to_update.save()
            return HttpResponseRedirect(reverse("movies:index"))
    else:
        update_form = Movie_Rating()

    return render(
        request,
        "movies/edit.html",
        {
            "form": update_form,
            "id": id,
            "movie": movie_to_update
        },
    )


def delete(request, id):
    movie_to_delete = Movie.objects.get(pk=id)
    movie_to_delete.delete()
    return HttpResponseRedirect(reverse("movies:index"))


def select(request, title):
    params = {"api_key": MDB_API_KEY, "query": title, "language": "en-US"}

    movie_search = requests.get("https://api.themoviedb.org/3/search/movie",
                                params=params)
    movie_search.raise_for_status()
    data = json.loads(movie_search.text)
    return render(request, "movies/select.html", {"movies": data})


def find(request, id):
    movie_id = id
    params = {"api_key": MDB_API_KEY, "language": "en-US"}
    movie_title_search = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}", params=params)
    movie_title_search.raise_for_status()
    data = json.loads(movie_title_search.text)
    img_id = data["poster_path"]
    add_movie_db = Movie(
        title=data["title"],
        year=data["release_date"][0:4],
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{img_id}",
    )
    add_movie_db.save()

    return HttpResponseRedirect(reverse("movies:index"))
