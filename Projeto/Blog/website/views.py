from django.shortcuts import render

def hello_blog(request):
    lista = ['nathan', 'marco', 'joao', 'carol', 'carla']
    data = {'name': 'Curso de django 3', 'lista_tec': lista}
    return render(request, 'index.html', data)