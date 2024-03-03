# Generated by Django 5.0.2 on 2024-03-02 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_delete_drivercar'),
        ('employees', '0006_drivercar'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDriverAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.car', verbose_name='Машина')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver', verbose_name='Водитель')),
            ],
            options={
                'verbose_name': 'Машина-Водитель',
                'verbose_name_plural': 'Машины-Водители',
                'db_table': 'cars_drivers_assignment',
                'unique_together': {('car', 'driver')},
            },
        ),
        migrations.DeleteModel(
            name='DriverCar',
        ),
    ]
