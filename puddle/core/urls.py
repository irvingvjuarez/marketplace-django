from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index, contact, browse, category_detail, sign_up
from .forms import LoginForm

app_name = "core"
urlpatterns = [
    path('', index, name="index"),
    path("contact/", contact, name="contact"),
    path("browse/", browse, name="browse"),
    path("signup/", sign_up, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
    path("category/<int:category_id>", category_detail, name="category_detail")
]
