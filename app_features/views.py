from django.shortcuts import render
from .models import Features

# Create your views here.



def movies(request):
    all_movies = Features.objects.order_by('price')
    context = {'movies': all_movies}
    return render(request, 'app_features/movies.html', context)


def movie(request, movie_id):
    one_movie = None
    try:
        one_movie = Features.objects.get(id=movie_id)
    except:
        print('หาไม่เจอ หรือเธอไม่มี')
    context = {'movie': one_movie}
    return render(request, 'app_features/movie.html', context)

def musics(request):
    return render(request, 'app_features/musics.html')

def promotions(request):
    return render(request, 'app_features/promotions.html')