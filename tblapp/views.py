from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tblapp.models import Course
from tblapp.models import Student
# Create your views here.
def home(request):
    return render(request,'home.html')

   
def addc(request):
    return render(request,'addcourse.html')
   


def adds(request):
   courses=Course.objects.all()
   return render(request,'addstudent.html',{'course':courses})
    

def show(request):
    
        student=Student.objects.all()
        return render(request,'show.html',{'students':student})
    
def addcdb(request):
    if request.method=="POST":
        course_name=request.POST.get('course_name')
        course_fee=request.POST.get('fee')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('/')
def addsdb(request):
    if request.method=='POST':
        student_name=request.POST['name']
        print(student_name)
        student_address=request.POST['address']
        print(student_address)
        age=request.POST['age']
        print(age)
        jdate=request.POST['jdate']
        print(jdate)
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('/')
def edit(request,pk):
    student=Student.objects.get(id=pk)
    courses=Course.objects.all()
    return render(request,'edit.html',{'student':student,'course1':courses})
def editdb(request,pk):
    if request.method=="POST":
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['name']
        
        student.student_address=request.POST['address']
        
        student.student_age=request.POST['age']
        
        student.joining_date=request.POST['jdate']
        
        sel=request.POST['sel']
      
        course1=Course.objects.get(id=sel)
        
        student.course=course1
        student.save()
        return redirect('show')  
    return render(request,'edit.html')
def deletepage(request,pk):
    emp=Student.objects.get(id=pk)
    emp.delete()
    return redirect('show')
    