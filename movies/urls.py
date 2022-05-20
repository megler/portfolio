from django.urls import path, include
from movies import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("add", views.add, name="add"),
    path("select/<str:title>", views.select, name="select"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("find/<int:id>", views.find, name="find"),
]
