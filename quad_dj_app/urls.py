from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('', views.new_game),
    path('vocabulary', views.vocabulary)
    # path('token', obtain_auth_token),
    # path('signup', views.signup),
    # path("profiles", views.profiles),
    # path("profiles/current", views.current_profile),
    ]