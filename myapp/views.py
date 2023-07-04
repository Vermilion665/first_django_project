import datetime

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .forms import CarForm, DriverForm, ClientForm
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
# Create your views here.

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Машины парка", 'url_name': 'cars'},
    {'title': "Водители парка", 'url_name': 'drivers'},
    {'title': "Клиенты", 'url_name': 'clients'},
    {'title': "Сотрудники", 'url_name': 'employees'},
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
    cars = Car.objects.all()
    context = {'title': title, 'menu': menu, 'cars': cars}
    return render(request, 'myapp/cars.html', context=context)


def drivers(request):
    title = 'Водители'
    drivers = Driver.objects.all()
    context = {'title': title, 'menu': menu, 'drivers': drivers}
    return render(request, 'myapp/drivers.html', context=context)


def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'myapp/clients.html', context=context)


# def employees(request):
#     title = 'Сотрудники'
#     employees = EmployeeList()
#     context = {'title': title, 'menu': menu, 'employees': employees}
#     return render(request, 'myapp/employee_list.html', context=context)

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





def add_car(request):
    title = 'Добавить машину'
    if request.method == 'GET':
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
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return drivers(request)
    else:
        form = DriverForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'myapp/driver_add.html', context=context)


def add_client(request):

    title = 'Добавить клиента'

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            age = datetime.date.today().year - form.cleaned_data['birthday'].year
            instance.age = age
            instance.save()
            # form.save()
            return clients(request)
    else:
        form = ClientForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'myapp/client_add.html', context=context)


def client_card(request, pk):
    title = 'Client info'
    # client = Client.objects.get(pk=pk)
    client = get_object_or_404(Client, pk=pk)
    context = {'menu': menu, 'title': title, 'client': client}

    return render(request, 'myapp/client_card.html', context=context)


def driver_card(request, pk):
    title = 'Driver info'
    driver = get_object_or_404(Driver, pk=pk)
    context = {'menu': menu, 'title': title, 'driver': driver}
    return render(request, 'myapp/driver_card.html', context=context)


def car_card(request, pk):
    title = 'Car info'
    car = get_object_or_404(Car, pk=pk)
    context = {'menu': menu, 'title': title, 'car': car}
    return render(request, 'myapp/car_card.html', context=context)


class EmployeeList(ListView):
    model = Employee
    # template_name = 'myapp/employee_list.html'
    context_object_name = 'employees'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сотрудники'
        context["count"] = Employee.objects.count()
        context['menu'] = menu
        return context


class EmployeeDetail(DetailView):
    model = Employee
    # template_name = 'myapp/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о сотруднике'
        context['menu'] = menu
        return context



class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'myapp/employee_form.html'

