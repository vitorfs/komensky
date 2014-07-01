# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    DISPONIVEL = 'D'
    RASCUNHO = 'R'
    CANCELADO = 'C'
    REJEITADO = 'E'
    PENDENTE = 'P'
    STATUS = (
        (DISPONIVEL, u'Disponível'),
        (RASCUNHO, u'Rascunho'),
        (CANCELADO, u'Cancelado'),
        (REJEITADO, u'Rejeitado'),
        (PENDENTE, u'Pendente de Aprovação'),
        )

    TECNOLOGIA_INFORMACAO = 'TI'
    LINGUAS = 'LI'
    MATEMATICA = 'MA'
    OUTRO = 'OU'
    SUBJECT = (
        (LINGUAS, u'Línguas'),
        (MATEMATICA, u'Matemática'),
        (TECNOLOGIA_INFORMACAO, u'Tecnologia da Informação'),
        (OUTRO, u'Outro'),
        )

    title = models.CharField('Título', max_length=255)
    description = models.TextField('Descrição', max_length=1000)
    subject = models.CharField(max_length=2, choices=SUBJECT)
    user = models.ForeignKey(User)
    create_date = models.DateTimeField('Data de Criação', auto_now_add=True)
    update_date = models.DateTimeField('Data de Atualização', blank=True)
    status = models.CharField(max_length=1, choices=STATUS)
    score = models.IntegerField('Pontuação', default=0)
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class Module(models.Model):
    VIDEO = 'V'
    TEXTO = 'T'
    MODULE_TYPE = (
        (VIDEO, u'Vídeo'),
        (TEXTO, u'Texto')
        )
    course = models.ForeignKey(Course)
    parent = models.ForeignKey('self')
    title = models.CharField(max_length=255)
    module_type = models.CharField(max_length=1, choices=MODULE_TYPE)