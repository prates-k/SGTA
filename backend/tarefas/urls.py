from django.urls import path
from .views import listar_tarefas, listar_tarefas_abertas, listar_tarefas_por_prioridade

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas/', listar_tarefas_abertas),
    path('tarefas/prioridade/<str:prioridade>/', listar_tarefas_por_prioridade),
]
