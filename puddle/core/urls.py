from django.urls import path
from .views import index, contact, browse, category_detail

urlpatterns = [
    path('', index, name="index"),
    path("contact/", contact, name="contact"),
    path("browse/", browse, name="browse"),
    path("category/<int:category_id>", category_detail, name="category_detail")
]
