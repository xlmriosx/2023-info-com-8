# Creating my first project Django
```
content-project/ (1) <--- Carpeta contenedora del proyecto
├── myenv/
├── myproject/ (2) <--- Carpeta del proyecto
│ ├── manage.py
│ ├── myproject/
│ │ ├── __init__.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── myapp/
│ │ ├── migrations/
│ │ ├── __init__.py
│ │ ├── admin.py
│ │ ├── models.py
│ │ ├── views.py
│ │ └── ...
│ └── ...
└── ...

(1) - Para ejecutar comandos del entorno(activarlo o desactivarlo)
- myenv\Scripts\activate
- myenv\Scripts\deactivate
- python -m pip install --upgrade pip
- pip install nombre_del_paquete
- etc

(2) - Para ejecutar comandos del manage.py
- pyhton manage.py runserver
- pyhton manage.py makemigrations
- pyhton manage.py migrate
- pyhton manage.py createsuperuser
- pyhton manage.py startapp myapp
- pip install nombre_del_paquete
- etc
```
## Commands

1. Creation of virtual environment
`python -m venv NEW_ENV` NEW_ENV puede tener cualqueir nombre

2. Activate virtual environment
`NEW_ENV\Scripts\activate` Windows estando fuera de la carpeta NEW_ENV
`Source ./bin/activate` Linux

2.1. Error? Ejecucion de scripts deshabilitada
    1. Get-ExecutionPolicy -list
    2. Set-ExecutionPolicy -Scope LocalMachine Bypass
    3. Ejecutar paso 2 `NEW_ENV\Scripts\activate`

3. Install Django
`pip install Django`

4. Create a project Django
`django-admin startproject INFO` INFO puede tener cualqueir nombre

5. Move to INFO directory
`cd INFO`

6. Run server Django
`python manage.py runserver`

7. Shut Down server
`CTRL + C`

8. Initialize an application with name like locro
`python manage.py startapp locro`

9. Apply migrations
`python manage.py migrate`

## Creating a Super User
`python manage.py createsuperuser`

OperationalError: no such table: auth_user --> Run `python manage.py migrate`

Link: http://localhost:8000/admin

## Configuration of database

- Install dependency
`pip install mysqlclient`

- In General/INFO/settings.py
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "informatorio",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```


