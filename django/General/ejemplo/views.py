from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# Create your views here.
from .models import Pregunta, Opcion

# def index(request):
#     pregunta_lista = Pregunta.objects
#     output = ", ".join([q.pregunta_texto for q in pregunta_lista])
#     return HttpResponse(output)

def index(request):
    pregunta_lista = Pregunta.objects.all()
    opcion_lista = Opcion.objects.all()
    template = loader.get_template("ejemplo/index.html")
    context = {
        "pregunta_lista": pregunta_lista,
        "opcion_lista": opcion_lista,
    }
    return HttpResponse(template.render(context, request))

def opciones(request):
    opcion_lista = Opcion.objects.all()
    template = loader.get_template("ejemplo/opciones.html")
    context = {
        "opcion_lista": opcion_lista,
    }
    return HttpResponse(template.render(context, request))

def preguntas(request):
    pregunta_lista = Pregunta.objects.all()
    template = loader.get_template("ejemplo/preguntas.html")
    context = {
        "pregunta_lista": pregunta_lista,
    }
    return HttpResponse(template.render(context, request))
