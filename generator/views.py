from django.shortcuts import render
#from django.http import HttpResponse
import random
# Create your views here.

def about(request):
    #return 'Hola wacho' # No podes devolver un string, tenes que convertirlo a una respuesta HTTP
    #return HttpResponse('Hello world') #No es lo mejor hacerlo asi, por eso creamos la carpeta Templates
    return render(request, 'generator/about.html') #Para esto, tambien hay que ir a Settings, y en InstalledApps, poner generator para especificar que hay una nueva app

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = int(request.GET.get('lenght')) # Siempre se envia como string asi que lo convertimos
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()_-'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    

    
    generated_password = ''
    for _ in range(lenght):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})