from django.db import models
from django.urls import reverse
from datetime import date
from phone_field import PhoneField


# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя водителя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия водителя')
    birthday = models.DateField(verbose_name='Дата рождения', default=date.today)
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=100, verbose_name='Город', null=True)
    passport = models.CharField(max_length=15, verbose_name='Паспорт', unique=True, default='')
    email = models.EmailField(verbose_name='Эл. почта', unique=True)
    is_activated = models.BooleanField(verbose_name='Активация', default=True)

    def __str__(self):
        return ''.join([str(self.first_name), str(self.first_name)])

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ['last_name', '-birthday'] # - obratnaya sortirovka
        unique_together = (
            ('first_name', 'last_name', 'passport')
        )


class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'


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
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['year', 'model']


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения', default=date.today)
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=50, verbose_name='Город')
    phone = PhoneField(blank=True, help_text='Vash nomer telefona', verbose_name='Телефон', unique=True)
    email = models.EmailField(verbose_name='Эл. почта', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([str(self.first_name), str(self.last_name)])

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['last_name']
        unique_together = (
            ('first_name', 'last_name', 'email')
        )


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
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

