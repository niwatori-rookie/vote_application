from django.db import models
import datetime
from django.utils import timezone
from accounts.models import CustomUser

# Create your models here.
#ER図にて、QuestionとChoiceは1対多の関係になる
class Question(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    


class Choice(models.Model):
    #ForeignKeyの場合、1つのQuestionに対して複数のChoiceが紐づく
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #各テーブルレコードを識別するための名前を返す
    def __str__(self):
        return self.choice_text

#admin
#username:niwatori,Email address:test@mail.com,Password:shota301

