import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date      = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # past 
        is_recent = self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        # not future 
        isnt_future = self.pub_date <= timezone.now()

        return is_recent and isnt_future

class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes       = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
