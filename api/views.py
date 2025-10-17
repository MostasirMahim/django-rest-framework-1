from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from students.models import Student
# Create your views here.

def studentsView(request):
    students = Student.objects.all()
    lists = list(students.values())
    return JsonResponse(lists, safe=False)