from django.db import models

from .enums import car_colors, car_categories

# Create your models here.


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
