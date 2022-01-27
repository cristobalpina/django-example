from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users', views.users),
    path('users/<name>', views.users_name),
]
