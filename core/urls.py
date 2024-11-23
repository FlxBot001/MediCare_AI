from django.contrib import admin
from django.urls import path
from . import views

appname = "core"
urlpatterns = [
    path('', views.home, name="Home"),
    path('', views.index, name='index'),
]
