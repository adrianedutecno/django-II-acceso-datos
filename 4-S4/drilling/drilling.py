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

# crear views para listar y agregar
	producto/views.py

# crear forms.py
	producto/forms.py
	form django import forms
	class ProductoForm(forms.ModelForm)
	
# crear carpeta/directorio templates dentro del aplicativo
  	producto/templates

# crear htmls para listar, agregar, editar, eliminar
	base.html
	layout.html
	footer.html
	navbar.html
	listar.html
	crear.html
	editar.html

# instalar librerias para formularios y bootstrap
	pip install crispy-bootstrap5
	pip install django-bootstrap-v5
	pip install django-crispy-forms

# configurar librerias
	config/settigs.py
	INSTALLED_APPS:
	'bootstrap5',  # bootstrap 5
    	'crispy_forms',  # crispy forms 
    	'crispy_bootstrap5'

	CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
	CRISPY_TEMPLATE_PACK = 'bootstrap5'

# configurar urls.py
	config/urls.py
	from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', include('producto.urls')),
]
	
# crear urls.py
	producto/urls.py

# levantar el proyecto
	python manage.py runserver