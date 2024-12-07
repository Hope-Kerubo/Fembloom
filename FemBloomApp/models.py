from django.db import models

# Create your models here.
class User(models.Model):
    Fullname = models.CharField(max_length=100)
    EmailAddress = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=100)

    def __str__(self):
        return self.Fullname

class Module(models.Model):
    module_name = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    def __str__(self):
        return self.module_name


