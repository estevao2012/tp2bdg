from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

from sistema.models import Projeto

import psycopg2
import json


class IndexView(generic.ListView):
    template_name = 'sistema/index.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()


class ProjetosView(generic.DetailView):
    model = User
    template_name = 'sistema/projetos.html'


def consultas(request, projeto_id):
    response_data = Projeto.objects.get(pk=projeto_id).consulta_set.all()
    data = serializers.serialize("json", response_data)
    return HttpResponse(
        json.dumps(data), content_type="application/json"
        )


#Pegar as variaveis POST e fazer conexao
def conexaoSession(request):

    return HttpResponse('OK')


def customSelect(request):

    conn = psycopg2.connect(database="iniciante", user="root", password="root", host="127.0.0.1")
    cursor = conn.cursor()
    cursor.execute("select * from visualize_choice")
    tudo = cursor.fetchall()
    tod = []
    for elem in tudo:
        tod.append(elem[2])

    return HttpResponse('<br>'.join(tod))
