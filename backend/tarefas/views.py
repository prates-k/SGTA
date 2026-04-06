from django.http import JsonResponse
from .models import Tarefa

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(status=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)
    

def buscar_tarefa_por_id(request, id):
    try:
        tarefa = Tarefa.objects.get(id=id)
        return JsonResponse({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'status': tarefa.status,
            'prioridade': tarefa.prioridade
        })
    except Tarefa.DoesNotExist:
        return JsonResponse({'erro': 'Tarefa não encontrada'}, status=404)
    
def listar_tarefas_abertas_urgentes(request):
    tarefas = Tarefa.objects.filter(
        status='ABERTA',
        prioridade='URGENTE'
    ).values()

    return JsonResponse(list(tarefas), safe=False)

from datetime import date

def listar_tarefas_atrasadas(request):
    hoje = date.today()

    tarefas = Tarefa.objects.filter(
        data_entrega__lt=hoje
    ).exclude(status='CONCLUIDA').values()

    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefas_por_titulo(request, palavra):
    tarefas = Tarefa.objects.filter(
        titulo__icontains=palavra
    ).values()

    return JsonResponse(list(tarefas), safe=False)