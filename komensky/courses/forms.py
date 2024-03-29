#coding: utf-8

from django import forms
from komensky.courses.models import Course, Module

class CourseForm(forms.ModelForm):
    title = forms.CharField(
        label='Título',
        widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=255,)
    description = forms.CharField(
        label='Descrição',
        widget=forms.Textarea(attrs={'class':'form-control'}), 
        max_length=1000,)
    subject = forms.ChoiceField(
        label='Categoria',
        choices=Course.SUBJECT, 
        widget=forms.Select(attrs={'class':'form-control'}),)

    class Meta:
        model = Course
        exclude = ('user', 'score', 'update_date', 'create_date', 'status',)

class ModuleForm(forms.ModelForm):
    title = forms.CharField(
        label='Título',
        widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=255,)
    content = forms.CharField(
        label='Conteúdo',
        widget=forms.Textarea(attrs={'class':'form-control'}), 
        max_length=4000,)
    module_type = forms.ChoiceField(
        label='Tipo',
        choices=Module.MODULE_TYPE, 
        widget=forms.Select(attrs={'class':'form-control'}),)

    class Meta:
        model = Module
        exclude = ('course', 'parent',)