# Generated by Django 3.2.7 on 2021-09-09 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0010_alter_films_film_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Director',
            new_name='Directors',
        ),
    ]
