from django.views import generic
from .models import Picture, Film
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, PictureForm
from django.shortcuts import render
import numpy as np
import pandas as pd



from popularity_based import Popularity_based

# set some print options
np.set_printoptions(precision=4)
np.set_printoptions(threshold=5)
np.set_printoptions(suppress=True)
pd.set_option('precision', 3, 'notebook_repr_html', True, )
# init random gen
np.random.seed(2)



users_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/ratings.csv"
movies_file = "/media/sourabhkondapaka/Sourabh's/main_project/sandbox/ml-latest-small/movies.csv"
users = pd.read_table(users_file,sep=',', header=None,names = ['user_id','movie_id','rating','timestamp'])
movies = pd.read_table(movies_file, sep=',')


pb = Popularity_based(users, movies)
pb.create()
top_movies = pb.recommend()





def index(request):
    if not request.user.is_authenticated():
        return render(request, 'movies/login.html')
    else:

        #moviez = Film.objects.all()
        #all_pictures = Picture.objects.all()    'all_pictures': all_pictures,
        #return render(request, 'movies/index.html', { 'moviez': moviez})        
        #pb = Popularity_based(users, movies)
        #pb.create()
        #top_movies = pb.recommend()
        return render(request, 'movies/index.html', {'top_movies': top_movies})


def detail(request, picture_id):
    if not request.user.is_authenticated():
        return render(request, 'movies/login.html')
    else:
        user = request.user
        picture = get_object_or_404(Picture, pk=picture_id)
        return render(request, 'movies/detail.html', {'picture': picture, 'user': user})


def podetail(request, film_id):
    if not request.user.is_authenticated():
        return render(request, 'movies/login.html')
    else:
        user = request.user
        film = get_object_or_404(Film, pk=film_id)
        return render(request, 'movies/popdetail.html', {'film': film, 'user': user})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'movies/index.html', {'top_movies': top_movies})

            else:
                return render(request, 'movies/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'movies/login.html',
                          {'error_message': 'Invalid login , Please Check your details correctly and try again'})
    return render(request, 'movies/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'movies/index.html', {'top_movies': top_movies})

    context = {
        "form": form,
    }
    return render(request, 'movies/register.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'movies/login.html', context)
