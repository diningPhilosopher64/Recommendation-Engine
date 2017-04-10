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
from collaborative_filtering import Collaborative_filtering


from updater import *

import imdb
from BeautifulSoup import BeautifulSoup
import urllib2 
import os
import requests
import bs4
import json,requests,unicodedata,urllib2
import time


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
# Remove the line below if it throws any error when using popularity based or collaborative_filtering
movies.columns = ['movie_id','title','genres']
ratings_file = "/home/sourabhkondapaka/Desktop/ratingsss.csv"

#Popularity_based code
pb = Popularity_based(users, movies)
pb.create()
top_movies = pb.recommend()

#Collaborative_filtering code
cf = Collaborative_filtering(ratings_file,movies)
cf.compute_svd()

#Details of movie code
ia = imdb.IMDb()
url = "http://www.omdbapi.com/?t="


#keys in json string are :
'''
[u'Plot', u'Rated', u'Title', u'Ratings',
 u'DVD', u'Writer', u'Production', u'Actors',
  u'Type', u'imdbVotes', u'Website', u'Poster', u'Director',
   u'Released', u'Awards', u'Genre', u'imdbRating',
    u'Language', u'Country', u'BoxOffice', u'Runtime',
     u'imdbID', u'Metascore', u'Response', u'Year']
'''



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


def detail(request, movie_id):
    if not request.user.is_authenticated():
        return render(request, 'movies/login.html')
    else:
        user = request.user
        #picture = get_object_or_404(Picture, pk=picture_id)
        #getting details from omdbapi
        bb = str(movies.ix[movies['movie_id'] == movie_id ]['title']).split()    
        q = bb.index('Name:')
        bb = ' '.join(bb[1:q])
        item = ia.search_movie(bb)[0]
        print("Name in item is " + str(item))
        name = str(item)        
        ll = name.split()
        #ll = '+'.join(ll)
        movie_url = url + '+'.join(ll)
        movie_url += "&plot=full"
        print movie_url
        content = urllib2.urlopen(movie_url).read()
        jsontopython = json.loads(content)

        #Values passed to details.html file
        plot = jsontopython['Plot']
        writers = jsontopython['Writer']
        producers = jsontopython['Production']
        actors = jsontopython['Actors']
        director = jsontopython['Director']
        awards = jsontopython['Awards']
        runtime = jsontopython['Runtime']
        genre = jsontopython['Genre']

        #movies similar to this movie.
        similar_movies = cf.get_similar_movies(movie_id)
        return render(request, 'movies/detail.html', {'similar_movies':similar_movies,'plot':plot,'writers':writers,'producers':producers, 'actors':actors,'director':director,'awards':awards,'runtime':runtime,'genre':genre})


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
