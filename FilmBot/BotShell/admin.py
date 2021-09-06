from django.contrib import admin

from .import models

#class FilmAdmin(admin.ModelAdmin):
   # list_display = ['pk', 'film_name', 'video_cotent']
   # list_editable = ['film_name']


#admin.site.register(models.Films, FilmAdmin)
class GenresAdmin(admin.ModelAdmin):
    list_display = ['pk', 'genre_name']
    list_editable = ['genre_name']

class Messagedmin(admin.ModelAdmin):
    list_display = ['__str__', 'msg_id']
   # list_editable = ['film_name']


admin.site.register(models.Films)
admin.site.register(models.Genres)
admin.site.register(models.Stars)
admin.site.register(models.Director)
admin.site.register(models.Comments)
admin.site.register(models.Users)
admin.site.register(models.Requests)
admin.site.register(models.Message, Messagedmin)