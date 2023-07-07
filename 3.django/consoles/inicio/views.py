from django.shortcuts import render

def view_inicio(request):
    return render(request, 'inicio/paginas/index.html')
