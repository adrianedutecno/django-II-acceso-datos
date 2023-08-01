# La fábrica de productos puede producir uno o más productos.

# El producto solo puede pertenecer a un fabricante

class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    
    
# realizar la migración, para guardar cambios en la base de datos

# python manage.py makemigrations

# python manage.py migrate