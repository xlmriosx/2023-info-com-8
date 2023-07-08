from django.urls import path

from . import views

app_name = "ejemplo"
urlpatterns = [
    path("", views.index, name="index"),
    path("opciones", views.opciones, name="opciones"),
    path("preguntas", views.preguntas, name="preguntas"),
]