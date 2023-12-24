from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create-contribution', views.create_contribution, name='create_contribution'),
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
    path('wallpaper-list/desktop', views.wallpaper_list, name="wallpaper_list"),
    path('wallpaper-list/mobile', views.wallpaper_list_mobile, name="wallpaper_list_mobile"),
    path('wallpaper-list/desktop/search', views.wallpaper_list_search, name="wallpaper_list_search"),
    path('wallpaper-list/mobile/search', views.wallpaper_list_mobile_search, name="wallpaper_list_mobile_search"),
    path('wallpaper/<int:id>', views.wallpaper, name="wallpaper"),
    path('increment_download_count/<int:wallpaper_id>/', views.increment_download_count, name='increment_download_count'),
    path('logout', LogoutView.as_view(), name='logout'),
]
