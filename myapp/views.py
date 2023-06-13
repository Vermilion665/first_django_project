from django.http import HttpResponse
from .forms import CarForm, DriverForm, ClientForm
from .models import Car, Client, Driver
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Машины парка", 'url_name': 'cars'},
    {'title': "Водители парка", 'url_name': 'drivers'},
    {'title': "Клиенты", 'url_name': 'clients'}
]


def index_main(request):
    return HttpResponse('<h1>Main page</h1>')  # Всегда веб-страничка долна возвращаться (результат ответа на запрос


def index_myapp(request):
    title = 'Моя главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/index.html', context=context)


def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/about.html', context=context)


def cars(request):
    title = 'Машины'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/cars.html', context=context)


def drivers(request):
    title = 'Водители'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/drivers.html', context=context)


@csrf_protect
def login(request):
    title = 'Войти'
    context = {'title': title, 'menu': menu}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'Login - {username}, Password - {password}')

    if request.method == 'GET':
        return render(request, 'myapp/login.html', context=context)


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')  # То, что мы передаем через ? &
    age = request.GET.get('age')
    # return HttpResponse(f'Page_contacts, id = {id}')
    get_params = {'mane': name, "age": age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params = {get_params}')


def clients(request):
    title = 'Клиенты'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/clients.html', context=context)


def add_car(request):
    if request.method == 'GET':
        title = 'Добавить машину'
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)

    if request.method == 'POST':
        carform = CarForm(request.POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.save()
        return cars(request)


def add_driver(request):
    title = 'Добавить водителя'
    form = DriverForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'myapp/driver_add.html', context=context)


def add_client(request):
    title = 'Добавить клиента'
    form = ClientForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'myapp/client_add.html', context=context)