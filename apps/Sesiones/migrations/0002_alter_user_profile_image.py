# Generated by Django 5.1.1 on 2024-10-21 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sesiones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='DefaultUser.png', null=True, upload_to='imagenes_perfil', verbose_name='Imagen de perfil'),
        ),
    ]
