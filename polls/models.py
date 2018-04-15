# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField('Nội dung',max_length=200)
    date_pub = models.DateTimeField('Ngày cập nhật',auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.date_pub >= timezone.now() - datetime.timedelta(days=1)
        # return 'My yahoo!'

    # was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField('Đáp án', max_length=200)
    votes = models.IntegerField('Số lần vote', default=0)
    def __str__(self):
        return self.choice_text