from django.db import models


class Requests(models.Model):
    film_name = models.CharField(max_length=100)
    id_tele = models.IntegerField(default=None)
    process = [
        ('🔄', '🔄'),
        ('✅', '✅'),
        ('⛔️', '⛔️'),
    ]

    verification_process = models.CharField(default='🔄', choices=process, max_length=2)

    def __str__(self):
        return str(self.film_name)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
