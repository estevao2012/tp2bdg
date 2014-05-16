from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from sistema.models import Projeto
from django.contrib.gis.geos import Point, GEOSGeometry
import psycopg2


class IndexView(generic.ListView):
    template_name = 'sistema/index.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()


class ProjetosView(generic.DetailView):
    model = User
    template_name = 'sistema/projetos.html'


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
def conexaoSession(request):
    try:
        request.session['database'] = 'iniciante'
        request.session['user'] = 'root'
        request.session['password'] = 'root'
        request.session['host'] = '127.0.0.1'
        return HttpResponse('OK')
    except Exception, e:
        return HttpResponse(e)


def customSelect(request):

    conn = psycopg2.connect(database="bdg", user="root", password="root", host="127.0.0.1")
    cursor = conn.cursor()
    cursor.execute("select * from geodata.armazens")
    tudo = cursor.fetchall()
    tod = []
    for elem in tudo:
        tod.append(GEOSGeometry(elem[8]).geojson)

    return HttpResponse(','.join(tod))
