from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Driver
from .forms import UserForm, DriverForm
from AutoparkProject.utils import calculate_age
from AutoparkProject.settings import LOGIN_REDIRECT_URL
from employees.models import Car, CarDriverAssignment

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
    form = AuthenticationForm(data=request.POST or None)

    if request.method == 'GET':
        return render(request, 'drivers/authorization.html', {'title': 'Войти | Водители', 'form': form})

    elif request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                url = request.GET.get('next', LOGIN_REDIRECT_URL)

                return redirect(url)
            

def log_out(request):
    logout(request)

    return redirect('drivers:get_main_page')
        

@login_required
def get_profile(request, pk):
    driver = get_object_or_404(Driver, pk=pk)

    car_driver_assignment = CarDriverAssignment.objects.filter(driver=driver).first()

    if car_driver_assignment is not None:
        car = car_driver_assignment.car
    else:
        car = None

    return render(request, 'drivers/profile.html', {'driver': driver, 'car': car})


@login_required
def show_available_cars(request):
    title = 'Машины | Водители'

    available_cars = Car.objects.filter(is_available=True)

    available_cars_count = available_cars.count()

    context = {'title': title, 'available_cars': available_cars, 'available_cars_count': available_cars_count}

    return render(request, 'drivers/available_cars.html', context)


def confirm_car_choice(request, pk):
    if request.method == 'GET':
        car = Car.objects.get(pk=pk)

        context = {'title': 'Подтверждение выбора машины', 'car': car}

        return render(request, 'drivers/car_choice_confirmation.html', context)
    
    elif request.method == 'POST':
        if request.POST.get('pk'):
            driver = Driver.objects.get(user=request.user)
            
            try:
                driver.cardriverassignment.car.is_available = True
                driver.cardriverassignment.car.save()

                driver.cardriverassignment.delete()
                
            except:
                pass
            
            car = Car.objects.get(pk=request.POST.get('pk'))

            car.is_available = False

            car.save()

            CarDriverAssignment.objects.create(car=car, driver=driver)

            return redirect('drivers:show_available_cars')
        
        else:
            return redirect('drivers:show_available_cars')
        

def give_up_car(request):
    if request.method == 'GET':
        return render(request, 'drivers/car_giving_up_confirmation.html')
    
    elif request.method == 'POST':
        driver = Driver.objects.get(user=request.user)

        if 'confirm' in request.POST:
            driver.cardriverassignment.car.is_available = True
            driver.cardriverassignment.car.save()

            driver.cardriverassignment.delete()

            return redirect('drivers:get_profile', pk=driver.id)

        if 'cancel' in request.POST:
            return redirect('drivers:get_profile', pk=driver.id)
