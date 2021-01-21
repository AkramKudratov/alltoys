from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from toys import views

urlpatterns = [
    path('', views.dashboard),
]