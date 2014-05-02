from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Projeto(models.Model):
    usuario = models.ForeignKey(User)
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome


class Consulta(models.Model):
    projeto = models.ForeignKey(Projeto)
    consulta = models.TextField()
    data = models.DateTimeField('date published')
    ordem = models.IntegerField()

    def __unicode__(self):
        return self.consulta
