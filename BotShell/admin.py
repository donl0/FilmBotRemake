from django.contrib import admin

from .import models


class FilmsAdminSite(admin.ModelAdmin):
    model = models.Requests
    list_display = ['pk', 'film_name', 'year', 'rating', 'likes', 'dislikes', 'comments_counter', 'watches24h']


class UsersAdminSite(admin.ModelAdmin):
    model = models.Requests
    list_display = ['pk', 'name', 'id_tele']


class RequestsAdminSite(admin.ModelAdmin):
    model = models.Requests
    fields = ['film_name', 'verification_process', 'id_tele']
    list_display = ['pk', 'film_name', 'verification_process', 'id_tele']
    actions = ['in_process_verification', 'apply_verification', 'canceled_verification']

    def in_process_verification(self, request, queryset):
        queryset.update(verification_process='🔄')

    def apply_verification(self, request, queryset):
        queryset.update(verification_process='✅')

    def canceled_verification(self, request, queryset):
        queryset.update(verification_process='⛔️')

class GenresAdmin(admin.ModelAdmin):
    list_display = ['pk', 'genre_name']
    list_editable = ['genre_name']


class Messagedmin(admin.ModelAdmin):
    list_display = ['__str__', 'msg_id']
   # list_editable = ['film_name']


admin.site.register(models.Films, FilmsAdminSite)
admin.site.register(models.Genres)
admin.site.register(models.Comments)
admin.site.register(models.Users, UsersAdminSite)
admin.site.register(models.Requests, RequestsAdminSite)
admin.site.register(models.Message, Messagedmin)
admin.site.register(models.Admins)
admin.site.register(models.Directors)
admin.site.register(models.Stars)
admin.site.register(models.GeneralHistory)
admin.site.register(models.TrendingFilms)
admin.site.register(models.LastSearch)