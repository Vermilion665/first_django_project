from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

menu = [{'title': 'O sayte', 'url_name': 'about'},
        {'title': 'Mashini parka', 'url_name': 'cars'},
        {'title': 'Voditeli parka', 'url_name': 'drivers'},
        ]


def index(request):
    return HttpResponse('<h1>Main page</h1>')


def index_myapp(request):
    title = 'moya glavnaya stranica'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/index.html', context=context)


def about(request):
    title = 'O sayte'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/about.html', context=context)


def login(request):
    return HttpResponse('Page_login')


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name': name, 'age': age}
    return HttpResponse(f'Page_contacts, url_parametr_id = {url_id}, get_params - {get_params}')


def cars(request):
    title = 'Mashini'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/cars.html', context=context)


def drivers(request):
    title = 'Voditeli'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/drivers.html', context=context)


