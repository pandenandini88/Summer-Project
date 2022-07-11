from django.urls import path

from . import views

urlpatterns = [
    path('', views.poll_index, name='poll_index'),
]