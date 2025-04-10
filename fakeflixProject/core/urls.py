from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.search, name="search"),
    path("login", views.login, name="login"),
    path("sign-up", views.signup, name="sign-up"),
    path("create-account", views.create_account, name="create-account"),
]
