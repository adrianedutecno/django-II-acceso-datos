"""
1. Obtener todas las fábricas y productos por medio de una consulta SQL, haciendo uso del método
raw(). Para los productos imprima la fábrica correspondiente.
"""
python manage.py shell

from producto.models import Producto, Fabrica

fabricas = Fabrica.objects.raw('select * from producto_fabrica')

print('\n'.join(str(i.nombre) for i in fabricas))

productos = Producto.objects.raw('select * from producto_producto')

print(', '.join(str(i.nombre) for i in productos))

"""
2. Realizar una consulta pasando los parámetros por raw que busque 
el producto “Protex Aloe”, y devuelva quien lo fabrica.
"""

producto = 'Protex Aloe'

consulta1 = Producto.objects.raw('select * from producto_producto where nombre = %s', [producto])

print(', '.join(str(i.fabrica) for i in consulta1))
        