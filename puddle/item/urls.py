from django.contrib import admin
from django.urls import path
from .views import detail, new

app_name = "item"
urlpatterns = [
    path('<int:item_id>/', detail, name="detail"),
    path("new/", new, name="new_item")
]