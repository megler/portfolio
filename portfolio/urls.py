from django.urls import path, include
from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("thanks", views.thanks, name="thanks"),
    path("twitter-about", views.twitter_about, name="twitter_about"),
    path("zscraper-about", views.zillow_about, name="zillow_about"),
    path("stocks-about", views.stocks_about, name="stocks_about"),
    path("movies-about", views.movies_about, name="movies_about"),
    path("blog-about", views.blog_about, name="blog_about"),
    path("auctions-about", views.auctions_about, name="auctions_about"),
    path("anf-about", views.anf_about, name="anf_about"),
]
