from django.contrib import admin
from django.urls import path
from .views import detail

urlpatterns = [
    path('<int:itemID>/', detail, name="detail"),
]