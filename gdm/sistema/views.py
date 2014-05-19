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
from psycopg2.extras import RealDictCursor
import datetime


class IndexView(generic.ListView):
    template_name = 'sistema/index.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()


def projetos(request, user_id, projeto_id=0):
    user = User.objects.get(pk=user_id)
    conexao = request.session
    if(projeto_id == 0):
        projeto = user.projeto_set.first
    else:
        try:
            projeto = Projeto.objects.get(pk=projeto_id)
        except Projeto.DoesNotExist:
            return redirect(reverse('sistema:projetos', args=(user_id,)))
    return render(
        request,
        'sistema/projetos.html',
        {"conexao": conexao, "projeto": projeto})


def consulta(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)
    return generateGeoJson(consulta.consulta, request.session)


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
    propriedades = request.POST.get('propriedades')
    projeto_id = request.POST.get('projeto_id')
    salvar = request.POST.get('salva')
    projeto = Projeto.objects.get(pk=projeto_id)
    consulta_nova = Consulta.create(consulta, projeto_id, propriedades)
    return generateGeoJson(consulta, request.session)


# Metodo Helper Para Gerar o GeoJson
def generateGeoJson(consulta, conexao):
    credentials = {'host': conexao['host'],
                   'database': conexao['database'],
                   'user': conexao['user'],
                   'password': conexao['password']}
    conn = psycopg2.connect(**credentials)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(consulta)
    tudo = cursor.fetchall()
    result = {}
    to_json = {
        'consulta': consulta
        }
    i = 0
    for elem in tudo:
        linhas = {}
        for key, value in elem.items():
            if key == 'geom':
                linhas[key] = GEOSGeometry(value).geojson
            else:
                linhas[key] = value
        result[str(i)] = linhas
        i = i+1        
    to_json['resultado'] = result
    return HttpResponse(
        simplejson.dumps(to_json, indent=4), mimetype="application/json"
        )
