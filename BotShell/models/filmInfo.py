from django.db import models
from .star import Stars
from .director import Directors
# Create your models here.


class Genres(models.Model):
    genre_name = models.CharField(verbose_name="name", max_length=30, default="NULL")

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name_plural = 'Genres'


class Films(models.Model):
    film_name = models.CharField(verbose_name="name", max_length=100, default="NULL", unique=True)
    year = models.CharField(max_length=5, default="NULL")
    rating = models.FloatField(default=0)
    genres = models.ManyToManyField(Genres, blank=True)

    description = models.CharField(max_length=1500, default="NULL")

    director = models.ManyToManyField(Directors, blank=True)
    stars = models.ManyToManyField(Stars, blank=True)

    video_link = models.CharField(verbose_name="video link", max_length=200, default="NULL")
    video_file = models.FileField(verbose_name='video', upload_to='videos/', default="NULL")

    trailer_link = models.CharField(verbose_name="trailer link", max_length=200,default="NULL")
    trailer_file = models.FileField(verbose_name='trailer', upload_to='videos/', default="NULL")

    photo = models.CharField(max_length=200, default="NULL")

    watches24h = models.IntegerField(default=0)
    watches7d = models.IntegerField(default=0)
    watches1m = models.IntegerField(default=0)
    watches_all = models.IntegerField(verbose_name='watches all', default=0)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments_counter = models.IntegerField(verbose_name='comments counter', default=0)

    def __str__(self):
        return self.film_name

    class Meta:
        verbose_name = 'film'
        verbose_name_plural = 'Films'
