from django import forms 
from django.contrib.auth.models import User

from .models import Picture

class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['picture_id', 'picture_title']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password'] 


