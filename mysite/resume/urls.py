from django.urls import path

from . import views

# maps the pages onto their respective urls, so resume/ will lead to the resume page
urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume')
]
