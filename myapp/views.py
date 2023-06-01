from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse('<h1>About site</h1>')

def login(request):
    return HttpResponse('Page_login')

def contacts(request):
    return HttpResponse('Page_contacts')
