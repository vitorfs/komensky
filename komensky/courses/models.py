# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    DISPONIVEL = 'D'
    RASCUNHO = 'R'
    CANCELADO = 'C'
    STATUS = (
        (DISPONIVEL, u'Disponível'),
        (RASCUNHO, u'Rascunho'),
        (CANCELADO, u'Cancelado'),
        )

    
    ARTES_DESIGN = 'AD'
    CIENCIAS_BIOLOGICAS = 'CB'
    CIENCIAS_EXATAS = 'CE'
    CIENCIAS_HUMANAS = 'CH'
    ADMINISTRACAO_CIENCIAS_CONTABEIS = 'AC'
    COMUNICACAO_SOCIAL = 'CS'
    DIREITO = 'DI'
    ECONOMIA = 'EC'
    EDUCACAO = 'ED'
    EDUCACAO_FISICA = 'EF'
    ENFERMAGEM = 'EN'
    ENGENHARIA = 'EG'
    FARMACIA = 'FA'
    FISIOTERAPIA = 'FI'
    LETRAS = 'LE'
    MEDICINA = 'ME'
    ODONTOLOGIA = 'OD'
    SERVICO_SOCIAL = 'SS'
    SUBJECT = (
        (ARTES_DESIGN, u'Artes e Design'),
        (CIENCIAS_BIOLOGICAS, u'Ciências Biológicas'),
        (CIENCIAS_EXATAS, u'Ciências Exatas'),
        (CIENCIAS_HUMANAS, u'Ciências Humanas'),
        (ADMINISTRACAO_CIENCIAS_CONTABEIS, u'Administração e Ciências Contábeis'),
        (COMUNICACAO_SOCIAL, u'Comunicação Social'),
        (DIREITO, u'Direito'),
        (ECONOMIA, u'Economia'),
        (EDUCACAO, u'Educação'),
        (EDUCACAO_FISICA, u'Educação Física'),
        (ENFERMAGEM, u'Enfermagem'),
        (ENGENHARIA, u'Engenharia'),
        (FARMACIA, u'Farmácia'),
        (FISIOTERAPIA, u'Fisioterapia'),
        (LETRAS, u'Letras'),
        (MEDICINA, u'Medicina'),
        (ODONTOLOGIA, u'Odontologia'),
        (SERVICO_SOCIAL, u'Serviço Social'),
        )

    title = models.CharField('Título', max_length=255)
    description = models.TextField('Descrição', max_length=100)
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
    TEXTUAL = 'T'
    MODULE_TYPE = (
        (VIDEO, u'Vídeo'),
        (TEXTUAL, u'Textual')
        )
    course = models.ForeignKey(Course)
    parent = models.ForeignKey('self')
    title = models.CharField(max_length=255)
    module_type = models.CharField(max_length=1, choices=MODULE_TYPE)