from django.db import models
from .filmInfo import Films
from .requestsDb import Requests


class Users(models.Model):
    name = models.CharField(verbose_name="name", max_length=50, default="NULL")
    id_tele = models.IntegerField(default=None)
    favourite = models.ManyToManyField(Films, blank=True, related_name="NULL")
    requests = models.ManyToManyField(Requests, blank=True, related_name="NULL")
    id_likes = models.CharField(verbose_name='id likes', max_length=1000, blank=True, default="")
    id_dislikes = models.CharField(verbose_name='id dislikes', max_length=1000, blank=True, default="")
    history = models.ManyToManyField(Films, blank=True, related_name=None)

    search_way_chose = [
        ('by_name', 'by name'),
        ('by_actor', 'by actor'),
        ('by_director', 'by director'),
        ('by_all', 'by all'),
    ]
    search_way = models.CharField(verbose_name='search way', blank=True, choices=search_way_chose, max_length=15)
    paper_count = models.IntegerField(verbose_name='paper count', default=5)