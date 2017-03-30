from django import forms 
from django.contrib.auth.models import User

from .models import Picture, Film

class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['picture_id', 'picture_title', 'genres', 'ratings', 'picture_logo']

class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ['film_id', 'film_title', 'pop_genres', 'pop_ratings', 'pop_picture_logo']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']



