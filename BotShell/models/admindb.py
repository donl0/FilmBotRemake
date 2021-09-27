from django.db import models
from .filmInfo import Films
from .userInfo import Users


class Admins(models.Model):
    admin_id = models.IntegerField(verbose_name="admin tg id", default=0)

    def __str__(self):
        return str(self.admin_id)

    class Meta:
        verbose_name_plural = 'Admins'
