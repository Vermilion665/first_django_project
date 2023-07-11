from django.db import models
from django.urls import reverse


# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя водителя')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    # is_activated = models.BooleanField(verbose_name='Activatsiya', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chelovek'
        verbose_name_plural = 'Ludi'


class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Car(models.Model):

    colors = (
        ('черный', 'черный'),
        ('желтый', 'желтый'),
        ('белый', 'белый'),
        ('синий', 'синий'),
        ('зеленый', 'зеленый'),
        ('красный', 'красный'),
    )

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=30, choices=colors, verbose_name='Цвет')
    power = models.IntegerField(verbose_name="Мощность'")
    year = models.IntegerField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        #return f'{self.brand} {self.model}'
        return ' '.join([str(self.brand), str(self.model)])

    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Tachki'


class Client(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=30, verbose_name='Город')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Эл. почта')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([self.name, self.last_name])

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Employee(models.Model):
    edu_choises = [('middle', 'среднее'),
                   ('high', 'высшее'),
                   ('professional', 'профессиональное'),
                   ]

    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    position = models.CharField(max_length=50, verbose_name='Должность')
    education = models.CharField(max_length=30, choices=edu_choises)

    def __str__(self):
        return ' '.join([self.firstname, self.lastname])

    def get_absolute_url(self):
        return reverse('myapp:employee_list')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, related_name='car', verbose_name='машина')
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name='driver', verbose_name='водитель')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='car', verbose_name='Клиент')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([str(self.id), str(self.client)])

    def get_absolute_url(self):
        return reverse('myapp:order_list')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

