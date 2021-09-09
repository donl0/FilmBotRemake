from django.db import models

class Stars(models.Model):
    name = models.CharField(max_length=100, default="NULL")

    def __str__(self):
        return self.name