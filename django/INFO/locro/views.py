from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<title>Info 2023</title><h1>Vendemos locro $800 la porcion</h1>")
# Create your views here.
