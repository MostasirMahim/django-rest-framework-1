from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def studentsView(request):
    students = [
        {
            "name": "Sergey",
            "age": 25
        },
        {
            "name": "Ivan",
            "age": 30
        }
    ]
    return JsonResponse(students, safe=False)