from django.http import JsonResponse
from .models import Tarefa

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)
