# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Question, Choice

# Create your views here.

def index(request):
    context = {
        'title': 'Trang chủ',
        'questions':get_list_or_404(Question)
    }
    return render(request,'index.html', context=context)

def detail(request, question_id):
    context = {
        'title':'Detail ß',
        'question': get_object_or_404(Question, pk=question_id)
    }
    return render(request,'detail.html',context=context)