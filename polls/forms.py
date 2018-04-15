# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import Question, Choice

class QuestionForm(ModelForm):
    question_text = forms.CharField(label='Nhập nội dung câu hỏi')
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text','votes']