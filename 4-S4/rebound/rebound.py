cd config

python manage.py shell

p = Producto(nombre='Crema Colgate', precio=1500, descripcion='Crema para el cepillo de dientes')
p.save()
Producto.objects.all()
Producto.objects.all().values()