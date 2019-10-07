from django.shortcuts import render,redirect
from App5.StudentForm import StudentForm
from django.http import HttpResponse

def stud(request):
    form=StudentForm()
    return render(request,'./templates/index.html',{'form':form})
#taking reference as form object

def hi(request):
    id=request.POST['id']
    name=request.POST['name']
    message=id+" "+name+"<br/><a href='../stud/'>Back</a>"
    return HttpResponse(message)