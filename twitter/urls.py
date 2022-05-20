from django.urls import path
from twitter import views

app_name = "twitter"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:pk>", views.user_profile, name="user_profile"),
    path("follow/<int:id>", views.follow, name="follow"),
    path("unfollow/<int:id>", views.unfollow, name="unfollow"),
    path("send-tweet/<int:pk>", views.send_tweet, name="send_tweet"),
    path("following/<int:pk>", views.user_following, name="user_following"),
    # API
    path("like", views.like, name="like"),
    path("get-tweet/<int:id>", views.get_tweet, name="get_tweet"),
    path("edit-tweet", views.edit_tweet, name="edit_tweet"),
]
