from datetime import datetime
from django.shortcuts import render
from django.http import request, response
# Create your views here.


def template(request):
    return render(request, "index.html")


def footer(request):
    return render(request, "footer.html")
