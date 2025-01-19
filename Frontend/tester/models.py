from django.db import models

# Create your models here.

class Question(models.Model):
    molecule_name = models.CharField(max_length = 200)
    molecule_formula = models.CharField(max_length = 200)
    question_date = models.DateTimeField("date presented")
    
    def __str__(self):
        return self.molecule_name

class Answer(models.Model):
    user_name = models.CharField(max_length = 200)
    user_answer = models.CharField(max_length = 200)
    correct = models.BooleanField("answer outcome")
    
    def __str__(self):
        return self.user_name
    
class User(models.Model):
    user_name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.user_name