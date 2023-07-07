from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Pregunta

# def index(request):
#     pregunta_lista = Pregunta.objects
#     output = ", ".join([q.pregunta_texto for q in pregunta_lista])
#     return HttpResponse(output)

def index(request):
    pregunta_lista = Pregunta.objects.all()
    template = loader.get_template("ejemplo/index.html")
    context = {
        "pregunta_lista": pregunta_lista,
    }
    return HttpResponse(template.render(context, request))
