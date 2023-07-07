from django.shortcuts import render
from . import models

def view_inicio(request):
    return render(request, 'playstation/paginas/index.html')

def view_lancamentos(request):
    lancamentos = models.Modelo.objects.all()
    dicionario = {'lanc': lancamentos}
    return render(request, 'playstation/paginas/lancamentos.html', context=dicionario)

def view_modelo(request, link_url):
    modelo = models.Modelo.objects.filter(link=link_url)

    dicionario = {'valor':modelo[0]}

    return render(request, 'playstation/paginas/modelo.html', context=dicionario)
