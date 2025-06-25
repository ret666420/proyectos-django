from django.db import models

class Alumnos(models.Model):  # Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat")  # Texto corto
    nombre = models.TextField()  # Texto largo
    carrera = models.TextField()
    imagen = models.ImageField( null=True,upload_to="fotos", verbose_name="Fotografias")  # Imagen, null=True permite que el campo sea opcional
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación
    updated = models.DateTimeField(auto_now=True)  # Fecha y hora de última actualización

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]  # Ordena del más reciente al más viejo

    def __str__(self):
        return self.nombre  # Retorna el nombre como representación del objeto
    