# Generated by Django 5.0.2 on 2024-03-02 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_alter_cardriverassignment_car_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cardriverassignment',
            table='car_driver_assignments',
        ),
    ]
