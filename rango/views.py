from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    html = '<html><body><a href="about">Rango says hey there partner</a></body></html>'
    return HttpResponse(html)

def about(request):
    html = '<html><body><a href="index">Rango says here is the about page.</a></body></html>'
    return HttpResponse(html)