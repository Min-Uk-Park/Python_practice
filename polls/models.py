from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# a = Question() a.__str__()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1) # ???????????
    
class choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

    
    
# makemigrate => 데이터 테이블 생성 위한 설계도 만듬
# migrate => 실제로 테이블 생성
# python manage.py shell # 파이썬 shell에 뛰어들어 API가지고 논다..(?)

# 그런데 migrate하고 나면 코드 수정 반영 안되나...?????????????????
# class 해석 그리고 render
