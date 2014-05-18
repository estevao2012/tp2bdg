from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse
from django.utils import simplejson
from sistema.models import Projeto, Consulta
from django.contrib.gis.geos import Point, GEOSGeometry
import psycopg2
import datetime


class IndexView(generic.ListView):
    template_name = 'sistema/index.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()


def projetos(request, user_id):
    user = User.objects.get(pk=user_id)
    conexao = request.session
    projeto = user.projeto_set.first
    return render(request, 'sistema/projetos.html', {"conexao": conexao, "projeto": projeto})


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


def novaConsulta(request):

    consulta = request.POST.get('consulta')
    projeto_id = request.POST.get('projeto_id')
    salvar = request.POST.get('salva')
    projeto = Projeto.objects.get(pk=projeto_id)
    consulta_nova = Consulta(
        consulta=consulta,
        projeto_id=projeto_id,
        data=datetime.date.today(),
        ordem=0)
    consulta_nova.save()
    conn = psycopg2.connect(
        database=request.session['database'],
        user=request.session['user'],
        password=request.session['password'],
        host=request.session['host'])
    cursor = conn.cursor()
    cursor.execute(consulta)
    tudo = cursor.fetchall()
    tod = []
    for elem in tudo:
        tod.append(GEOSGeometry(elem[8]).geojson)

    to_json = {
        'projeto': {
            'nome': projeto.nome, 'id': projeto_id
            }
        }

    to_json['consultas'] = tod

    return HttpResponse(
        simplejson.dumps(to_json, indent=4), mimetype="application/json"
        )
