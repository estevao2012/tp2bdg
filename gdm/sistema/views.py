from django.views import generic
from django.contrib.auth.models import User
from sistema.models import Projeto


class IndexView(generic.ListView):
    template_name = 'sistema/index.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()


class ProjetosView(generic.DetailView):
    model = User
    template_name = 'sistema/projetos.html'


class ConsultasView(generic.DetailView):
    model = Projeto
    template_name = 'sistema/consultas.html'
