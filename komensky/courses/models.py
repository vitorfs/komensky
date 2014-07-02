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
    subject = models.CharField('Categoria', max_length=2, choices=SUBJECT)
    user = models.ForeignKey(User)
    create_date = models.DateTimeField('Data de Criação', auto_now_add=True)
    update_date = models.DateTimeField('Data de Atualização', auto_now_add=True)
    status = models.CharField('Status', max_length=1, choices=STATUS, default=RASCUNHO)
    score = models.IntegerField('Pontuação', default=0)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __unicode__(self):
        return self.title

    def get_status_as_label(self):
        label = 'default'
        if self.status == Course.DISPONIVEL:
            label = 'success'
        elif self.status == Course.REJEITADO or self.status == Course.CANCELADO:
            label = 'danger'
        elif self.status == Course.PENDENTE:
            label = 'warning'
        return u'<span class="label label-{0}">{1}</span>'.format(label, self.get_status_display())

    def get_modules(self):
        return Module.objects.filter(course=self)

class Module(models.Model):
    VIDEO = 'V'
    TEXTO = 'T'
    MODULE_TYPE = (
        (VIDEO, u'Vídeo'),
        (TEXTO, u'Texto')
        )

    course = models.ForeignKey(Course)
    parent = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField('Título', max_length=255)
    module_type = models.CharField('Tipo', max_length=1, choices=MODULE_TYPE)
    content = models.TextField('Conteúdo', max_length=4000, null=True, blank=True)
    create_date = models.DateTimeField('Data de Criação', auto_now_add=True)
    update_date = models.DateTimeField('Data de Atualização', auto_now_add=True)

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'

    def __unicode__(self):
        return self.title

    def get_module_type_as_icon(self):
        if self.module_type == Module.VIDEO:
            return u'<i class="fa fa-video-camera"></i>'
        elif self.module_type == Module.TEXTO:
            return u'<i class="fa fa-file-text-o"></i>'
        else:
            return u''