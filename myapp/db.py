# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Student
from django.shortcuts import redirect
import time

def search(request):  
    request.encoding='utf-8'

    list = Student.objects.all()

    # filter
    if 'searchFirstName' in request.GET:
        if request.GET['searchFirstName']!='':
            list = list.filter(firstName=request.GET['searchFirstName'])  
    if 'searchLastName' in request.GET:
        if request.GET['searchLastName']!='':
            list = list.filter(lastName=request.GET['searchLastName']) 
    if 'searchCity' in request.GET:
        if request.GET['searchCity']!='':
            list = list.filter(city=request.GET['searchCity'])
    if 'searchState' in request.GET:
        if request.GET['searchState']!='Choose State':
            list = list.filter(state=request.GET['searchState'])
    if 'searchMajor' in request.GET:
        if request.GET['searchMajor']!='':
            list = list.filter(major=request.GET['searchMajor']) 
    if 'searchStudentNumber' in request.GET:
        if request.GET['searchStudentNumber']!='':
            list = list.filter(studentNumber=request.GET['searchStudentNumber']) 
    if 'searchGender' in request.GET:
        if request.GET['searchGender']!='Choose Gender':
            list = list.filter(gender=request.GET['searchGender']) 


    l={}
    l['s']=list
    return render(request, "list.html", l)

def create(request):
    s = Student(firstName=request.POST['createFirstName'],lastName=request.POST['createLastName'],city=request.POST['createCity'],state=request.POST['createState'],major=request.POST['createMajor'],studentNumber=request.POST['createStudentNumber'],gender=request.POST['createGender'])
    s.save()
    # redirect to student profile page
    url="student/?message=The+new+student+profile&studentID="+str(s.id)
    return redirect(url)

def delete(request):
    data = request.GET
    stu = Student.objects.get(id=data["id"])
    stu.delete()
    return redirect("../index/")

def edit(request):
    data = request.POST
    s = Student.objects.get(id=data["id"])
    s.firstName = data['editFirstName']
    s.lastName = data['editLastName']
    s.city = data['editCity']
    s.state = data['editState']
    s.major = data['editMajor']
    s.studentNumber = data['editStudentNumber']
    s.gender = data['editGender']
    s.save()
    # redirect to student profile page
    url="student/?message=The+student+profile+has+been+updated&studentID="+str(s.id)
    return redirect(url)


