from django.db import models
from .filmInfo import Films


class TrendingFilms(models.Model):
    film_name = models.ForeignKey(Films, on_delete=models.CASCADE)
    # films that admin add by himself

    def __str__(self):
        return str(self.film_name)

    class Meta:
        verbose_name = 'Trending Film'
        verbose_name_plural = 'Trending Films'
