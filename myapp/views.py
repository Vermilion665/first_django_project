from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1>Main page</h1>')


def index_myapp(request):
    return HttpResponse('<h1>Myapp page</h1>')

def about(request):
    return HttpResponse('<h1>About site</h1>')


def login(request):
    return HttpResponse('Page_login')


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name': name, 'age': age}
    return HttpResponse(f'Page_contacts, url_parametr_id = {url_id}, get_params - {get_params}')


