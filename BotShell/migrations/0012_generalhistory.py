# Generated by Django 3.2.7 on 2021-09-10 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0011_rename_director_directors'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BotShell.films')),
            ],
        ),
    ]
