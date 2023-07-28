from datetime import datetime
from django.shortcuts import render
from django.http import request, response
# Create your views here.


def template(request):
    return render(request, "inicio.html", {'Titulo': 'Seformer'})

def sobre_nosotros(request):
   return render(request, "sobre_nosotros.html", {'Titulo': 'Seformer'})



