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



class Institution(models.Model):
    name = models.CharField(max_length=100, unique=True)
    county = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, default="Not Provided")


    def __str__(self):
        return f"{self.name} ({self.county})"


class UserAnswer(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Option, on_delete=models.CASCADE)


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/')  # Optional: for event image

    def __str__(self):
        return self.name