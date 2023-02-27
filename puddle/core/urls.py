from django.urls import path
from .views import index, contact, browse, category_detail, sign_up

app_name = "core"
urlpatterns = [
    path('', index, name="index"),
    path("contact/", contact, name="contact"),
    path("browse/", browse, name="browse"),
    path("signup/", sign_up, name="signup"),
    path("category/<int:category_id>", category_detail, name="category_detail")
]
