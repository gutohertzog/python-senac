from django.shortcuts import render

def view_index(request):
    dicionario = {'produtos':range(4), 'listas':range(3)}
    return render(request, 'lojinha/paginas/index.html', context=dicionario)

def view_search(request):
    dicionario = {'produtos':range(40)}
    return render(request, 'lojinha/paginas/search.html', context=dicionario)

