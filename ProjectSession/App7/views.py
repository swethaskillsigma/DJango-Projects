from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def setsession(request):
    request.session['sname']='Swetha'
    request.session['semail']='swetha@gmail.com'
    return HttpResponse("session is set")

def getsession(request):
    studentname=request.session['sname']
    studentemail=request.session['semail']
    return HttpResponse(studentname+" "+studentemail)

