from django.conf.urls import patterns, url
from sistema import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<user_id>\d+)/projetos/$', views.projetos, name='projetos'),  # User Id Pk
    url(r'^(?P<user_id>\d+)/projetos/(?P<projeto_id>\d+)$', views.projetos, name='projetos'),  # User Id Pk
    url(r'^consulta/(?P<consulta_id>\d+)$', views.consulta, name='consulta'),  # Url Recebida por ajax
    url(r'^salva-conexao/$', views.salvaConexao, name='salva-conexao'),
    url(r'^salva-consulta/$', views.novaConsulta, name='salva-consulta'),  # Envia Consulta
)
