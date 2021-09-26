from django.db import models
from .filmInfo import Films
from .requestsDb import Requests


class Users(models.Model):
    name = models.CharField(verbose_name="name", max_length=50, default="name_NULL1")
    id_tele = models.IntegerField(default=None)
    favourite = models.ManyToManyField(Films, blank=True, related_name="NULL2")
    requests = models.ManyToManyField(Requests, blank=True, related_name="NULL3")
    liked_films = models.ManyToManyField(Films, blank=True, related_name="NULL4")
    disliked_films = models.ManyToManyField(Films, blank=True, related_name="NULL5")
    history = models.ManyToManyField(Films, blank=True, related_name=None)

    search_way_chose = [
        ('by name', 'by name'),
        ('by actor', 'by actor'),
        ('by director', 'by director'),
        ('by all', 'by all'),
    ]
    search_way = models.CharField(verbose_name='search way', default='by name', choices=search_way_chose, max_length=15)
    paper_count = models.IntegerField(verbose_name='paper count', default=5)

    def __str__(self):
        return self.name+', '+str(self.id_tele)

