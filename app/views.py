from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from .functions import handle_uploaded_file
from django.http import HttpResponse

def index(request):  
    if request.method == 'POST':  
        form = StudentForm(request.POST, request.FILES)  
        if form.is_valid():  
            handle_uploaded_file(request.FILES['file'])
            form.save()
            return redirect('/show')  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})

def show(request, ):
    employees = Student.objects.all()
    return render(request, 'show.html', {'employees': employees})

def edit(request, id):
    employee = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'employee': employee})

def delete(request, id):
    employee = Student.objects.get(id=id)
    employee.delete()
    return redirect('/show')

    

