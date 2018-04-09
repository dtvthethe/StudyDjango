# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('Nội dung',max_length=200)
    date_pub = models.DateTimeField('Ngày cập nhật')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField('Đáp án', max_length=200)
    votes = models.IntegerField('Số lần vote', default=0)