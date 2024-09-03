from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'País de origen'
        verbose_name_plural = 'Países de origen'


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='País de origen'
    )

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
