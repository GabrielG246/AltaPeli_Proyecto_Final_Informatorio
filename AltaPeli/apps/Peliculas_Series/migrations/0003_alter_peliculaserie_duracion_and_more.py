# Generated by Django 5.1.1 on 2024-10-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas_Series', '0002_peliculaserie_portada_img_peliculaserie_trailer_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculaserie',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='peliculaserie',
            name='trailer_url',
            field=models.URLField(default='https://www.youtube.com/watch?v=dQw4w9WgXcQ', max_length=500),
        ),
    ]