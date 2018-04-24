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

class AuthenticateForm(forms.Form):
    username = forms.CharField(label='Ten dang nhap')
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username is None and password is None:
            raise forms.ValidationError(
                    "Tieu de"
                    "Tieu de 2"
                )
