from django.db import models

# Create your models here.


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
