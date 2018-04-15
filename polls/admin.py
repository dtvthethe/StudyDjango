# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Choice, Question
# Register your models here.

class ChoiceInline(admin.TabularInline): #StackedInline and TabularInline
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        # ('Date information', {'fields': ['date_pub'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'date_pub', 'was_published_recently']
    list_filter = ['date_pub']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
