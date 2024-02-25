from django.contrib import admin

from .models import Department, Position, CarBrand, Car

# Register your models here.

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(CarBrand)
admin.site.register(Car)
