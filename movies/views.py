from django.views import generic
from .models import Picture
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, PictureForm

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'movies/login.html')
    else:
        all_pictures = Picture.objects.all()
        return render(request, 'movies/index.html', {'all_pictures': all_pictures})

def detail(request, picture_id):
    if not request.user.is_authenticated():
        return render(request, 'movies/login.html')
    else:
        user = request.user
        picture = get_object_or_404(Picture, pk=picture_id)
        return render(request, 'movies/detail.html', {'picture': picture, 'user': user})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_pictures = Picture.objects.all()
                return render(request, 'movies/index.html', {'all_pictures': all_pictures})

            else:
                return render(request, 'movies/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'movies/login.html', {'error_message': 'Invalid login , Please Check your details correctly and try again'})
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
                all_pictures = Picture.objects.all()
                return render(request, 'movies/index.html', {'all_pictures': all_pictures})

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

         
