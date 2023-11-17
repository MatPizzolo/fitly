from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

def login_view(request):
    form_class = CustomAuthenticationForm

    if request.method == 'POST':
        form = form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = form_class()

    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})


def index_view(request):
    print(request.user)
    return render(request, 'index.html', {'user': request.user})

def clases_view(request):
    return render(request, 'clases.html', {'user': request.user})

def confirmacionContrato_view(request):
    return render(request, 'confirmacion-contrato.html', {'user': request.user})

def confirmacionRecuperar_view(request):
    return render(request, 'confirmacion-recuperar.html', {'user': request.user})

def contacto_view(request):
    return render(request, 'contacto.html', {'user': request.user})

def contratarAvanzado_view(request):
    return render(request, 'contratar-avanzado.html', {'user': request.user})

def contratarBasico_view(request):
    return render(request, 'contratar-basico.html', {'user': request.user})

def contratarPremium_view(request):
    return render(request, 'contratar-premium.html', {'user': request.user})

def instalaciones_view(request):
    return render(request, 'instalaciones.html', {'user': request.user})

def recuperarContraseña_view(request):
    return render(request, 'recuperar-contrasea.html', {'user': request.user})

def tarifas_view(request):
    return render(request, 'tarifas.html', {'user': request.user})
    

