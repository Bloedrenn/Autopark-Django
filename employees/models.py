from django.db import models
from django.contrib.auth.models import User

from .enums import car_colors, car_categories
from drivers.models import Driver

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

        db_table = 'autopark_departments'

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions', verbose_name='Отдел')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

        db_table = 'autopark_positions'

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(editable=False, verbose_name='Возраст')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

        db_table = 'autopark_employees'

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])


class CarBrand(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'Бренд машины'
        verbose_name_plural = 'Бренды машин'

        db_table = 'autopark_car_brands'

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Бренд')
    model = models.CharField(max_length=20, verbose_name='Модель')
    color = models.CharField(max_length=20, choices=car_colors, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год')
    image = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name='Фото')
    category = models.CharField(max_length=10, choices=car_categories, verbose_name='Категория')
    is_available = models.BooleanField(default=True, editable=False, verbose_name='Доступна')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

        db_table = 'autopark_cars'

    def __str__(self):
        return ' '.join([self.brand.name, self.model, str(self.year)])


class CarDriverAssignment(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, verbose_name='Машина')
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, verbose_name='Водитель')

    class Meta:
        verbose_name = 'Машина-Водитель'
        verbose_name_plural = 'Машины-Водители'

        db_table = 'car_driver_assignments'
