# -*- coding: UTF-8 -*-
from django.db import models
import datetime
from django.utils import timezone
#每个模型被表示为 django.db.models.Model 类的子类
class Question(models.Model):
    question_text = models.CharField(max_length = 200) #类变量，表示模型里的一个数据库字段,每个字段都是 Field 类的实例
    pub_date = models.DateTimeField('date published') #charField,DateTimeField,告诉数据处理的类型
    def __str__(self): #插入-str-方法
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text    
    
