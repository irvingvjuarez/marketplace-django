from django.urls import path
from .views import index, contact, browse

urlpatterns = [
    path('', index, name="index"),
    path("contact/", contact, name="contact"),
    path("browse/", browse, name="browse")
]
