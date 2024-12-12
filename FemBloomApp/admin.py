from django.contrib import admin
from FemBloomApp.models import Module, Quiz, Question, Option, Signup, Signin, Institution, UserAnswer, Event


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1  # Number of empty option rows to display by default

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of empty question rows to display by default

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    inlines = [QuestionInline]  # Add questions inline within the quiz admin page

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    search_fields = ('text',)
    inlines = [OptionInline]  # Add options inline within the question admin page

class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    search_fields = ('text',)

# Register your models here.
admin.site.register(Signup)
admin.site.register(Signin)
admin.site.register(Module)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Institution)
admin.site.register(UserAnswer)
admin.site.register(Event)