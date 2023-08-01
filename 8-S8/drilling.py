"""
1. Obtenga los campos de nombre, precio, y fecha de vencimiento de los productos.
"""
consulta1 = Producto.objects.raw('select nombre, precio, fecha_vencimiento from producto_producto')
print(', '.join(str(i.fabrica) for i in consulta1))

"""
2. Obtenga los productos donde el precio sea menor o igual a 2500, y muestre solo los campos de nombre y precio, respectivamente.
"""

consulta2 = Producto.objects.raw('select id, nombre, precio from producto_producto where precio <= %s', [2500])
print('\n'.join(str(i.nombre) for i in consulta2))
print('\n'.join(str(i.precio) for i in consulta2))
print('\n'.join(str(i.nombre + ' ' + str(i.precio)) for i in consulta2))

'select nombre, precio from producto_producto where precio <= 2500'

"""
3. Modifique haciendo uso de SQL personalizado y cursores, la fábrica con nombre P&G en el país que se encuentra asignada a EEUU, o a Canadá.
"""
from django.db import connection

pais = 'Canada'
fabrica = 'P&G'

cursor = connection.cursor()
cursor.execute('UPDATE producto_fabrica set pais = %s where nombre = %s', [pais, fabrica])

cursor.execute('UPDATE producto_fabrica set pais = %s where nombre = %s', ['EEUU', 'Colgate'])


cursor.execute('select * from producto_fabrica')
row = cursor.fetchall()

query = """
        SELECT p.id, p.nombre as producto_nombre, p.precio, f.id as fabrica_id, f.nombre as fabrica_nombre
        FROM producto_producto p
        INNER JOIN producto_fabrica f ON p.fabrica_id = f.id
        WHERE p.precio <= %s;
        """

consulta = Producto.objects.raw(query, [2500])
print('\n'.join(str(i.nombre) for i in consulta))
print('\n'.join(str(i.nombre + ' ' + str(i.precio)) for i in consulta))