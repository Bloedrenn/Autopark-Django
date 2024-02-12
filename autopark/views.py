from django.shortcuts import render
from django.views.generic import CreateView

from .models import Driver
from .forms import DriverForm

# Create your views here.


# ------------ Driver ------------ #
class AddDriver(CreateView):
    model = Driver
    form_class = DriverForm
    template_name = 'autopark/add_driver_form.html'
