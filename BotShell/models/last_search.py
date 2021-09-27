from django.db import models
from .filmInfo import Films


class LastSearch(models.Model):
    film_name = models.ForeignKey(Films, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.film_name)

    class Meta:
        verbose_name = 'Last search films'
        verbose_name_plural = 'Last search films'
