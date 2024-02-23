from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .models import Driver
from .forms import UserForm, DriverForm
from AutoparkProject.utils import calculate_age
from AutoparkProject.settings import LOGIN_REDIRECT_URL

# Create your views here.


def get_main_page(request):
    return render(request, 'drivers/index.html', {'title': 'Главная страница | Водители'})


def register(request):
    if request.method == 'GET':
        user_form = UserForm()
        driver_form = DriverForm()

        context = {'user_form' : user_form, 'driver_form': driver_form}

        return render(request, 'drivers/registration.html', context)

    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        driver_form = DriverForm(request.POST)

        if user_form.is_valid() and driver_form.is_valid():
            user = user_form.save()
            driver = driver_form.save(commit=False)

            driver.user = user
            driver.age = calculate_age(driver.birthday)

            driver.save()

            return show_user_info_after_registration(request, driver)
        

def show_user_info_after_registration(request, driver):
    context = {'title': 'Регистрация завершена | Водители', 'driver': driver}

    return render(request, 'drivers/registration_completed.html', context)


def log_in(request):
    if request.method == 'GET':
        form = AuthenticationForm()

        return render(request, 'drivers/authorization.html', {'title': 'Войти | Водители', 'form': form})

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                url = request.GET.get('next', LOGIN_REDIRECT_URL)

                return redirect(url)
        

def get_profile(request, pk):
    driver = Driver.objects.get(pk=pk)

    return render(request, 'drivers/profile.html', {'driver': driver})
