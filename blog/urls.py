from django.urls import path
from django.views.generic import TemplateView

from blog import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="posts"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post"),
    path("about", TemplateView.as_view(template_name="blog/about.html"), name="about"),
]
