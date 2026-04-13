from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=60)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Evento(models.Model):
    nombre = models.CharField(max_length=45)
    fecha = models.DateField()
    # Esta es la clave foránea que conecta con Ubicacion
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre