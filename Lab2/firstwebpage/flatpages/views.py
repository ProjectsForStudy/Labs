from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'flatpages/static_handler.html')

def hello(request):
    return HttpResponse(u'Привет, Мир!')