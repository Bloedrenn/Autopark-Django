from django.db import models

from .enums import car_colors, car_categories

# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(editable=False, verbose_name='Возраст')
    is_available = models.BooleanField(default=False, verbose_name='Доступен')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

        db_table = 'autopark_drivers'

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
    

class CarBrand(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

        db_table = 'autopark_car_brands'


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Бренд')
    model = models.CharField(max_length=20, verbose_name='Модель')
    color = models.CharField(max_length=20, choices=car_colors, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год')
    image = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name='Фото')
    category = models.CharField(max_length=10, choices=car_categories, verbose_name='Категория')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

        db_table = 'autopark_cars'

    def __str__(self):
        return ' '.join([self.brand, self.model, self.year])


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(editable=False, verbose_name='Возраст')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        db_table = 'autopark_clients'

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
