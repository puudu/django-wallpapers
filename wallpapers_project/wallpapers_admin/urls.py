from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('contributions', views.contributions, name='contributions'),
    path('categories', views.categories, name='categories'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:id>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:id>/delete/', views.category_delete, name='category_delete'),
]
