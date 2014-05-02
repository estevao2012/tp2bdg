from django.conf.urls import patterns, url
from sistema import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/projetos/$', views.ProjetosView.as_view(), name='projetos'),
    url(r'^(?P<pk>\d+)/consultas/$', views.ConsultasView.as_view(), name='consultas'),
)
