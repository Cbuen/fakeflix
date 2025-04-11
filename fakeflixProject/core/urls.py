from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.search, name="search"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("sign-up", views.signup, name="sign-up"),
    path("create-account", views.create_account, name="create-account"),
    path("account-manage", views.account_manage, name="account-manage"),
    path("change-password", views.changePassword, name="change-password"),
]
