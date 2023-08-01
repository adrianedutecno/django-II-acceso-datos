cd config

python manage.py shell

from producto.models import Producto, Fabrica

f = Fabrica(nombre='Colgate')
f.save()

f = Fabrica.objects.create(nombre='Colgate')

p = Producto(nombre='Colgate 360', precio=1850, descripcion='Crema dental', fabrica=f)
p.save()

Producto.objects.create(nombre='Protex Aloe', precio=1250, descripcion='Jabón de baño', fabrica=f)
Producto.objects.all()
Producto.objects.all().values()