from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Student
def students (request):
    students = Student.objects.all()
    return JsonResponse(list(students.values()), safe=False)