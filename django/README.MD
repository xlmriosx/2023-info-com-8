# Creating my first project Django

## Commands

1. Creation of virtual environment
`python -m venv NEW_ENV` NEW_ENV puede tener cualqueir nombre

2. Activate virtual environment
`NEW_ENV\Scripts\activate` Windows
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

7. Initialize an application
`python manage.py startapp locro`

8. Apply migrations
`python manage.py migrate`

