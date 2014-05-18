from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Projeto(models.Model):
    usuario = models.ForeignKey(User)
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ["pk"]


class Consulta(models.Model):
    projeto = models.ForeignKey(Projeto)
    consulta = models.TextField()
    data = models.DateTimeField('date published')
    ordem = models.IntegerField()

    def __unicode__(self):
        return self.consulta

    @classmethod
    def create(cls, consulta, projeto, ordem):
        consultas = cls.objects.filter(consulta=consulta, projeto_id=projeto)
        if(consultas.count == 0):
            consulta = cls(
                consulta=consulta,
                projeto_id=projeto,
                ordem=ordem,
                data=datetime.date.today())
            consulta.save()
        else:
            consulta = consultas.first
        return consulta

