from django.db import models

class NombreURL(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.nombre