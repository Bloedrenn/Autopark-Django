from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
# from django.contrib.auth.forms import AuthenticationForm

from .forms import UserForm, ClientForm, CustomAuthenticationForm
from .models import Client
from AutoparkProject.utils import calculate_age

# Create your views here.


def get_main_page(request):
    return render(request, 'clients/index.html', {'title': 'Главная страница | Клиенты'})


def register(request):
    if request.method == 'GET':
        user_form = UserForm()
        client_form = ClientForm()

        context = {'user_form' : user_form, 'client_form': client_form}

        return render(request, 'clients/registration.html', context)

    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST)

        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save(commit=False)

            client.user = user
            client.age = calculate_age(client.birthday)

            client.save()

            return show_user_info_after_registration(request, client)
        

def show_user_info_after_registration(request, client):
    context = {'title': 'Регистрация завершена | Клиенты', 'client': client}

    return render(request, 'clients/registration_completed.html', context)


class UserLoginView(LoginView):
    # form_class = AuthenticationForm
    form_class = CustomAuthenticationForm

    template_name = 'clients/authorization.html'

    extra_context = {'title': 'Войти | Клиенты'}

    def get_success_url(self):
        return reverse_lazy('clients:get_main_page')


class UserLogoutView(TemplateView):
    template_name = 'clients/log_out_confirmation.html'

    def post(self, request):
        if 'confirm' in request.POST:
            logout(request)

        return redirect('clients:get_main_page')


class UserProfileView(DetailView):
    model = Client

    template_name = 'clients/profile.html'

    context_object_name = 'client'
