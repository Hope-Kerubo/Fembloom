from django.db import models

# Create your models here.
class Signup(models.Model):
    Fullname = models.CharField(max_length=100)
    EmailAddress = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=100)
    def __str__(self):
        return self.Fullname

class Signin(models.Model):
    Fullname = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    def __str__(self):
        return self.Fullname

class Module(models.Model):
    module_name = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    def __str__(self):
        return self.module_name



class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} (Correct: {self.is_correct})"



