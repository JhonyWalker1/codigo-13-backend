from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app_index(request):
    #return HttpResponse("Hola nuevamente")
    titulo = "Encuesta"
    context = {
        'titulo': titulo
    }
    
    return render(request, 'index.html', context)

def detalle(request,pregunta_id):
    return HttpResponse('pregunta nro %s.' % pregunta_id)