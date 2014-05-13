from django.conf.urls import patterns, url
from sistema import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/projetos/$', views.ProjetosView.as_view(), name='projetos'),  # User Id Pk
    url(r'^(?P<projeto_id>\d+)/consultas/$', views.consultas, name='consultas'),  # Url Recebida por ajax
    url(r'^conecta/$', views.conexaoSession, name='conecta'),
    url(r'^teste/$', views.customSelect, name='teste'),  # Teste de Consultas
)
