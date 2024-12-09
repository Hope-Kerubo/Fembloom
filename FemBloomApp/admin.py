from django.contrib import admin
from FemBloomApp.models import User
from FemBloomApp.models import Module
from FemBloomApp.models import Quiz
from FemBloomApp.models import Question
from FemBloomApp.models import Option


# Register your models here.
admin.site.register(User)
admin.site.register(Module)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)