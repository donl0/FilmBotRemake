from django.db import models
from .filmInfo import Films


class GeneralHistory(models.Model):
    film_name = models.ForeignKey(Films, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.film_name)
