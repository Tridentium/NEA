from django.db import models

# Create your models here.

class Question(models.Model):
    question_id = models.IntegerField()
    molecule_name = models.CharField(max_length = 200)
    question_date = models.DateTimeField("date presented")
    outcome = models.BooleanField()
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
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_class = models.CharField(max_length=200)
    
    # # Create a new linking table to allow for storage of multiple questions
    # most_recent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_name