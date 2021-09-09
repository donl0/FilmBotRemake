from django.db import models
from .filmInfo import Films

class GeneralHistory(models.Model):
    film_name = models.ForeignKey(Films)