from django.conf.urls import patterns, url
from sistema import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<user_id>\d+)/projetos/$', views.projetos, name='projetos'),  # User Id Pk
    url(r'^(?P<projeto_id>\d+)/consultas/$', views.consultas, name='consultas'),  # Url Recebida por ajax
    url(r'^salva-conexao/$', views.salvaConexao, name='salva-conexao'),
    url(r'^teste/$', views.customSelect, name='teste'),  # Teste de Consultas
)
