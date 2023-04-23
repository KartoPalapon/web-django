from django.urls import path
from . import views

urlpatterns = [
#    path('', views.index, name='index'),
    path('movie/', views.movies, name='movies'),
    path('movie/<int:movie_id>', views.movie, name='movie'),
    path('music/', views.musics, name='musics'),
    path('promotion/', views.promotions, name='promotions'),
]