# Generated by Django 3.2.7 on 2021-09-11 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0012_generalhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BotShell.films')),
            ],
        ),
    ]
