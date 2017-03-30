from django.contrib.auth.models import Permission, User
from django.db import models
from decimal import Decimal


class Picture(models.Model):
    user = models.ForeignKey(User, default=1)
    picture_id = models.IntegerField(default=0)
    picture_title = models.CharField(max_length=500)
    genres = models.CharField(max_length=1000)
    ratings = models.DecimalField(max_digits=10, decimal_places=1)
    picture_logo = models.CharField(max_length=1000, default='/media/noimage.jpg')

    def __str__(self):
        return self.picture_title


class Film(models.Model):
    film_id = models.IntegerField(default=0)
    film_title = models.CharField(max_length=500)
    pop_genres = models.CharField(max_length=1000)
    pop_ratings = models.DecimalField(max_digits=10, decimal_places=1)
    pop_picture_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.film_title
