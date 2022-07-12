from django.urls import path

from . import views

# maps the pages onto their respective urls, so resume/ will lead to the resume page
urlpatterns = [
    path('', views.poll_index, name='poll_index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    


]