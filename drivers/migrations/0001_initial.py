# Generated by Django 5.0.2 on 2024-02-22 20:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('age', models.IntegerField(editable=False, verbose_name='Возраст')),
                ('is_available', models.BooleanField(default=False, verbose_name='Доступен')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
                'db_table': 'autopark_drivers',
            },
        ),
    ]
