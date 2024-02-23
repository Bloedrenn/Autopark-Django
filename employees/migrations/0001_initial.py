# Generated by Django 5.0.2 on 2024-02-22 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'db_table': 'autopark_car_brands',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, verbose_name='Модель')),
                ('color', models.CharField(choices=[('Black', 'Чёрный'), ('Red', 'Красный'), ('Blue', 'Синий'), ('Purple', 'Фиолетовый')], max_length=20, verbose_name='Цвет')),
                ('power', models.IntegerField(verbose_name='Мощность')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Фото')),
                ('category', models.CharField(choices=[('Business', 'Бизнес'), ('Comfort', 'Комфорт'), ('Econom', 'Эконом')], max_length=10, verbose_name='Категория')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='employees.carbrand', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'db_table': 'autopark_cars',
            },
        ),
    ]
