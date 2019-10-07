from django.shortcuts import render,redirect
from App6.models import Stud
from django.http import HttpResponse
from ProjectDataModels import settings

# Create your views here.
def loadMe(request):
       return render(request,'./templates/RegForm.html')

#Insert Operation
def crudops(request):
    #create an entry
        stud=Stud(
        stud_name=request.GET['sname'],
        stud_course=request.GET['scourse']
        )    
        stud.save()#acts like commit
        return redirect('../viewAll')

#Select Operation
def viewAll(request):
    objs=Stud.objects.all()
    root="<table border='1'><tr><th>ID</th><th>Student Name</th><th>Course</th></tr>"
    res=" "
    for cl in objs:
        res=res+"<tr><td>"+str(cl.id)+"</td><td>"+cl.stud_name+"</td><td>"+cl.stud_course+"</tr>"
    root=root+""+res+"</table>"  
    root=root+"<a href='../loadMe'>Back</a>"
    return HttpResponse(root)

#Select by condition
def filterByCourse(request,course):
    objs=Stud.objects.filter(stud_course=course)
    res="<br/>"
    for cl in objs:
        res=res+cl.stud_name+" "+cl.stud_course+"<br/>"
    return HttpResponse(res)

#Deletion of records
def delStud(request,id):
    stud=Stud.objects.get(id=id)
    stud.delete()
    return redirect('../viewAll')


