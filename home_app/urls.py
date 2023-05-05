# import modules
from django.urls import path, include
from .views import (
    home_view,
    login_view,
    logout_view,
    profile_view,
)

urlpatterns = [
    path("", home_view, name="homepage"),
    path("login", login_view, name="loginpage"),
    path("logout", logout_view, name="logoutpage"),
    path("student-dashboard/", profile_view, name="student-dashboard"),
]