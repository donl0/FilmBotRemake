from django.db import models
from .filmInfo import Films
from .userInfo import Users

class Comments(models.Model):
    text = models.CharField(max_length=1000, default="NULL")
    #user = models.ManyToManyField()
    film_name = models.ForeignKey(Films, on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Comments'
