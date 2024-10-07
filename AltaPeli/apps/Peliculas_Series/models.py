from django.db import models

from apps.Actores_Directores.models import Director
from apps.Actores_Directores.models import Actor
from AltaPeli.models import Premio
from django.contrib.auth.models import User


# Create your models here.

# Modelo Genero
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    
# Modelo Tipo
class Tipo(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    

# Modelo Pelicula/Serie
class PeliculaSerie(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    duracion = models.IntegerField()
    anio_estreno = models.SmallIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

# Modelo Reparto (Tabla Intermedia entre Peliculas y Actores)
class Reparto(models.Model):
    pelicula_serie = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    
    
# Modelo Puntuación (Tabla Intermedia entre Peliculas y Usuario)
class Puntuacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula_serie = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    comentario = models.TextField(max_length=400)

    def __str__(self):
        return f'Puntuación de {self.usuario} para {self.pelicula_serie}'
    
    
# Tabla Intermedia entre Actor, Premio y Película
class ActorPeliculaPremio(models.Model):
    pelicula = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)
    
    
    
    
# Tabla Intermedia entre Director, Premio y Película
class DirectorPeliculaPremio(models.Model):
    pelicula = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)