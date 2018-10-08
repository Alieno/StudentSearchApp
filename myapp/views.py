from django.shortcuts import render
from myapp.models import Student

# Create your views here.
def index(request):
	return render(request, "index.html", {})

def student(request):
	data = request.GET
	stu = Student.objects.get(id=data["studentID"]) 

	return render(request, "student.html", {"message":data["message"], "student":stu})


def edit(request):
	data = request.GET
	stu = Student.objects.get(id=data["id"]) 

	return render(request, "edit.html", {"student":stu})