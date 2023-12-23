from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('contributions', views.contributions, name='contributions')
]
