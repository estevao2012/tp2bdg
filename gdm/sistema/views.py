from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse
from django.utils import simplejson
from sistema.models import Projeto
from django.contrib.gis.geos import Point, GEOSGeometry
import psycopg2


class IndexView(generic.ListView):
    template_name = 'sistema/index.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()


def projetos(request, user_id):
    user = User.objects.get(pk=user_id)
    conexao = request.session
    return render(request, 'sistema/projetos.html', {"conexao": conexao})


def consultas(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    consultas = projeto.consulta_set.all()
    to_json = {
        'projeto': {
            'nome': projeto.nome, 'id': projeto.id
            }
        }
    to_json['consultas'] = serializers.serialize('json', consultas)

    return HttpResponse(
        simplejson.dumps(to_json, indent=4), mimetype="application/json"
        )


#Pegar as variaveis POST e fazer conexao
def salvaConexao(request):
    user_id = request.POST.get('usuario_id')

    try:
        database = request.POST.get('database')
        host_db = request.POST.get('host')
        user_db = request.POST.get('user')
        pass_db = request.POST.get('pass')

        request.session['database'] = database
        request.session['user'] = user_db
        request.session['password'] = pass_db
        request.session['host'] = host_db
        request.session['conectado'] = True
        return redirect(reverse('sistema:projetos', args=(user_id,)))
    except Exception, e:
        request.session['conectado'] = False
        return redirect(reverse('sistema:projetos', args=(user_id,)))


def customSelect(request):

    consulta = request.POST.get('consulta')
    conn = psycopg2.connect(
        database="bdg",
        user="root",
        password="root",
        host="127.0.0.1")
    cursor = conn.cursor()
    cursor.execute(consulta)
    tudo = cursor.fetchall()
    tod = []
    for elem in tudo:
        tod.append(GEOSGeometry(elem[8]).geojson)

    return HttpResponse(','.join(tod))
