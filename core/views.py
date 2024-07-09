from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Las contraseñas no coinciden'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'El nombre de usuario ya existe'})

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'signup.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Procesar los datos (enviar correo, guardar en base de datos, etc.)
        send_mail(
            f'Mensaje de {name}', 
            message, 
            email, 
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        
        # Puedes agregar lógica para mostrar un mensaje de éxito o redirigir a otra página
        return redirect('contacto')

    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def test(request):
    return render(request, 'test.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('success'))
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})