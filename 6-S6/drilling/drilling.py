"""
Agregue los siguientes campos a los modelos,y genere las migraciones correspondientes.
Fábrica: pais= Tipo cadena de 100 caracteres.
Producto: fecha_vencimiento= Tipo fecha, que puede ser nulo o vacío
"""


class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=50, blank=True, null=True)

    # producto = models.ManyToManyField(Producto)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)