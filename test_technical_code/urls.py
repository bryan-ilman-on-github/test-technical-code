from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.show_homepage, name='homepage'),
    path('backend', views.backend, name='backend'),
]
