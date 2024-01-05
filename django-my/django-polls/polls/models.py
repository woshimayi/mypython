import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now().date()
        print("%s\n%s\n%s\n" % (now, now - datetime.timedelta(days=1), self.pub_date))
        return now - datetime.timedelta(days=1) <= self.pub_date <= now






class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)