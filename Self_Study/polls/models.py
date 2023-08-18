import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# one to many model

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField("date published")

  def __str__(self) -> str:
    return self.question_text

  def was_published_recently(self):
    #  어제 이후로 발행된 시간 반환 = 현재시각 - 하루전날의 시간 
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# 외래키는 Question이라는 데이터모델을 참조
# CASCADE는 Question이라는 데이터모델이 삭제되면 같이 삭제된다는 뜻..

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  Choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self) -> str:
    return self.Choice_text
