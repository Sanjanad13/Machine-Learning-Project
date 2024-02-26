from django.contrib import admin
from django.urls import path
from basics.views import *
urlpatterns = [
    path("galactic/",galactic,name="galactic"),
]
