import datetime
from django.db import models
from django.utils import timezone
# models contain essential fields and behaviour of the data you're storing
# in our poll app we'll create two models


class Question(models.Model):
    #the following are class variables each of which represents a database field
    question_text=models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # each Choice is related to a single Question
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
    is_fav=models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

    #through the following Django can
    #1. create a database schema(create table statements for this app
    #2. create a python-access API for accessing Question and Choice objects


    #migrations are how Django stores changes to your models
