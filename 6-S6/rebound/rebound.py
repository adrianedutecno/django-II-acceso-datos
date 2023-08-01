"""
1.Partiendo  del  modelo  creado  en el  CUE  anterior, 
relacionado al  modelo  de  fábricas  y  productos, 
liste todas las migraciones realizadas e indique porqué 
se crea el archivo 0001_inicial.py.
"""

python manage.py showmigrations

"""
2.¿Cuál es el comando que permite observar el SQL antes de aplicar una determinada migración, por ejemplo la 0001_inicial.py?
"""
python manage.py sqlmigrate app migration_name

"""
3.¿Cuáles son las claves primarias de los modelos?
"""
('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
