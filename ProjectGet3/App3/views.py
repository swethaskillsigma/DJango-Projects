from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loadPage(request):
    return render(request,'./templates/FileApp.html')

def viewData(request):
    name=request.GET['tname']
    return HttpResponse("Hello..."+name)
    