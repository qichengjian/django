from django.urls import path
from django.http import HttpRequest
from . import views

urlpatterns = [
    path("", views.index),
    path("new", views.new)
]