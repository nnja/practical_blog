from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>/", views.post, name="post"),
    path("about", views.index, name="about"),
]
