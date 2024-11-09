from django.db import models

class trivia(models.Model):
    ques=models.CharField(max_length=300)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    correct_ans=models.CharField(max_length=200)