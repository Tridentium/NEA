from django.db import models

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.molecule_name

class Answer(models.Model):
    def __str__(self):
        return self.user_name
    
class User(models.Model):
    # # Create a new linking table to allow for storage of multiple questions
    # most_recent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_name