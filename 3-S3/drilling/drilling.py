# instalar postgres como base de datos
# instalar pgadmin como gestor de base de datos
# crear database
	CREATE DATABASE db_practica_orm;
# crear usuario
	CREATE USER user_db WITH PASSWORD 'user_db';
# asignar permisos al usuario
	GRANT ALL PRIVILEGES ON DATABASE db_practica_orm TO postgres;
	GRANT ALL PRIVILEGES ON DATABASE db_practica_orm TO user_db;
# crear el proyecto
	pip install django
	django-admin startproject config
# crear la aplicación
	cd config
	django-admin startapp producto
# configurar base de datos
	conector db:
		pip install psycopg2
	config/settings.py:
		agregar configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # database to use
        'NAME': 'db_practica_orm',  # database name
        'USER': 'postgres',  # user database
        'PASSWORD': 'admin',  # password user database
        'HOST': '127.0.0.1',  # localhost
        'PORT': '5432',  # database port number
    }
}		
# crear modelos
# realizar migraciones
	python manage.py makemigrations
	python manage.py migrate
	python manage.py sqlmigrate aplicacion 0001