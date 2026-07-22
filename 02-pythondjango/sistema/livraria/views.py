from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
 
from django.http import HttpResponse
 
# Create your views here.
 
def inicio(request):
   # return HttpResponse("<h1>Boas vindas a Livraria Ana Cunha</h1>")
    return render(request, 'pages/inicio.html')

def sobre(request):
    return render(request, 'pages/sobre.html')

def livros(request):
    return render(request, 'livros/index.html')

def criar(request):
    return render(request, 'livros/criar.html')




