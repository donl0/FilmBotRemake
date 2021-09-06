from django.db import models

class Requests(models.Model):
    name = models.CharField(max_length=100)
