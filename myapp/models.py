from django.db import models

# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя водителя')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    #is_activated = models.BooleanField(verbose_name='Activatsiya', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chelovek'
        verbose_name_plural = 'Ludi'


class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    power = models.IntegerField(verbose_name="Мощность'")
    year = models.IntegerField(verbose_name='Год выпуска')

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