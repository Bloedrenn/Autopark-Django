from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
