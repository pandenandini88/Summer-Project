from django.urls import path

from . import views

# maps the pages onto their respective urls, so resume/ will lead to the resume page
urlpatterns = [
    path('', views.poll_index, name='poll_index'),
]