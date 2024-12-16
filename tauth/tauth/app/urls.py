from django.urls import path

from . import views

urlpatterns = [
    path("", views.t_auth),
    path("logout/", views.t_logout),
    path("can-login/", views.can_login),
]