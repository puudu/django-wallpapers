from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create-contribution', views.create_contribution, name='create_contribution'),
    path('wallpaper-list', views.wallpaper_list, name="wallpaper_list"),
    path('wallpaper/<int:id>', views.wallpaper, name="wallpaper"),
    path('increment_download_count/<int:wallpaper_id>/', views.increment_download_count, name='increment_download_count'),
    path('logout', LogoutView.as_view(), name='logout'),
]
