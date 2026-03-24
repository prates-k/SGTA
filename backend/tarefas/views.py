from django.http import JsonResponse
from .models import Tarefa

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)