python manage.py shell

# 1. Obtenga todos los registros de fábricas y productos.
from producto.models import Producto, Fabrica

productos = Producto.objects.all().values() # select * from producto
fabricas = Fabrica.objects.all().values() # select * from Fabrica

productos
fabricas

# 2. Obtenga los campos de nombre, precio, y fecha de vencimiento 
# de los productos. 
# Demuestre también cuál es la consulta SQL que se genera del ORM.
consulta1 = productos.values_list('nombre', 'precio', 'fecha_vencimiento')

consulta1
str(consulta1.query)
str(productos.values_list('nombre', 'precio', 'fecha_vencimiento').query)

# 3. Obtenga los productos donde el precio sea menor o igual a 2500, 
# mostrando solo los campos de nombre y precio, respectivamente. 
# Demuestra también cuál es la consulta SQL que se genera del ORM.
consulta2 = productos.filter(precio__lte=2500).values('nombre', 'precio')

consulta2
str(consulta2.query)

consulta3 = productos.filter(precio__gte=2500).values('nombre', 'precio')

consulta3

# 4. Consulte los productos que se vencen antes del año 2024, 
# e imprima el nombre, precio, f_vencimiento, y fabricante. 
# Demuestre también cuál es la consulta SQL que se genera del ORM.
consulta4 = productos.filter(fecha_vencimiento__lte='2023-12-31').values('nombre', 'precio', 'fecha_vencimiento')

str(consulta4.query)

consulta5 = productos.filter(fecha_vencimiento__year__lt='2024').values('nombre', 'precio', 'fecha_vencimiento')

str(consulta5.query)


producto_5 = Producto.objects.select_related('fabrica').get(id=5)
producto_5 = Producto.objects.select_related('fabrica').all()
producto_5 = Producto.objects.select_related('fabrica').get(id=5).nombre