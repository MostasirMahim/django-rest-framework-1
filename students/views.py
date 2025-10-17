from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def students (request):
    return HttpResponse([{
        "name": "Sergey",
        "age": 25
    }])