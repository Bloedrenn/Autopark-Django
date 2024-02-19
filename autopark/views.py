from datetime import date
from django.shortcuts import render, redirect

from .models import Driver
from .forms import UserForm, DriverForm

# Create your views here.


# ------------ Driver ------------ #
def calculate_age(birthday):
    today = date.today()

    temp_age = today.year - birthday.year

    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        temp_age -= 1

    age = temp_age

    return age


def register_driver(request):
    if request.method == 'GET':
        user_form = UserForm()
        driver_form = DriverForm()

        context = {'user_form' : user_form, 'driver_form': driver_form}

        return render(request, 'autopark/driver_registration.html', context)

    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        driver_form = DriverForm(request.POST)

        if user_form.is_valid() and driver_form.is_valid():
            user = user_form.save()
            driver = driver_form.save(commit=False)

            driver.user = user
            driver.age = calculate_age(driver.birthday)

            driver.save()

            return redirect('autopark:get_driver_profile', pk=driver.id)
        

def get_driver_profile(request, pk):
    driver = Driver.objects.get(pk=pk)

    return render(request, 'autopark/driver_profile.html', {'driver': driver})
