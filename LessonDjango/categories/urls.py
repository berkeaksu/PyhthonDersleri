from django.contrib import admin
from django.urls import path
from . import views #views.py içerisinde yer alan tüm viewları import eder.

urlpatterns = [
    path('', views.index, name = "index"),
]