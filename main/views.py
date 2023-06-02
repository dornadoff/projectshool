from django.shortcuts import render
from django.views import View
from .models import *

class StudentsView(View):
    def get(self, request):
        data = {
            "student": Student.objects.all().order_by("full_name")
        }
        return render(request, "students.html", data)

class StudentView(View):
    def get(self, request, pk):
        a = Student.objects.get(id=pk)
        b = []
        for i in a.full_name.split(" "):
            b.append(i)
        data = {
            "student": Student.objects.get(id=pk),
            "familiya": b[0],
            'name': b[1],
            'soc_set': SocialMedia.objects.filter(student__id=pk)
        }
        return render(request, "student.html", data)

class HomePage(View):
    def get(self, request):
        return render(request, "home_page.html")