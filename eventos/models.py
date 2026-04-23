from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=60)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'

class Persona(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

class Evento(models.Model):
    nombre = models.CharField(max_length=45)
    fecha = models.DateField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    asistentes = models.ManyToManyField(Persona, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'