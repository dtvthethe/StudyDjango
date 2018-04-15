# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import RequestContext
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Question, Choice

from .forms import QuestionForm, ChoiceForm

from django.forms.models import inlineformset_factory

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

def add(request):
    # question = Question.objects.get(pk=5)
    question = Question()
    ChoiceInlineFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=2, can_delete=True)
    form =  QuestionForm(instance=question, prefix="main")
    formset = ChoiceInlineFormSet(instance=question, prefix="nested")
    context = {
        'title':'Add question',
        'form':form,
        "formset": formset
    }
    if(request.method == 'POST'):
        #form = AuthorForm(request.POST, request.FILES, instance=author, prefix="main")
        form = QuestionForm(request.POST, instance=question, prefix="main")
        formset = ChoiceInlineFormSet(request.POST,instance=question, prefix="nested")
        if(form.is_valid() and formset.is_valid()):
            #post = form.save(commit = True)
            # post.author = request.user
            # post.published_date = timezone.now()
            # post.save()
            form.save()
            formset.save()
    return render(request, 'add.html', context=context)


def update(request, question_id = None):
    if question_id == None:
        raise Exception('Khong dc bo trong ID :D') 
    question = Question.objects.get(pk=question_id)
    ChoiceInlineFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=1, can_delete=True)
    form =  QuestionForm(instance=question, prefix="main")
    formset = ChoiceInlineFormSet(instance=question, prefix="nested")
    context = {
        'title':'Update question',
        'form':form,
        "formset": formset
    }
    return render(request, "update.html", context=context)

def handler404(request):
    return render(request, "404.html")

def handler500(request):
    return render(request, "500.html")