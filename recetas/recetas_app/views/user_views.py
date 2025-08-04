from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.urls import reverse



def registro(request):

    contexto = {}
    if request.method == "POST":
        print("POST")
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_exist = User.objects.filter(username = username).exists()
        if user_exist:
            error = "El nombre de usuario ya existe"
            contexto['error'] = error
            contexto['nombre'] = nombre
            contexto['apellido'] = apellido
            contexto['username'] = username
            contexto['email'] = email
        else:
            print("Crear usuario")
            User.objects.create_user(username, email, password, first_name=nombre, last_name=apellido)
            url = "{}?greetings=true".format(reverse('login'))
            return redirect()

    else:
        print("GET")
    return render(request, "usuario/registro.html", contexto)


def login(request):
    contexto = {}

    if request.method == "GET":
        greetings = request.GET.get('greetings')
        print("greetings: {}".format(greetings))
        if greetings == "true":
            contexto['mensaje'] = "Cuenta creada con éxito, por favor autentícate"

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect(reverse('home'))
        else:
            contexto['error'] = "Usuario o contraseña incorrectos"
    return render(request, 'usuario/login.html', contexto)

def logout(request):
    auth_logout(request)
    return redirect(reverse('home'))
