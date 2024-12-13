from django.contrib import admin
from FemBloomApp.models import (Module, Quiz, Question, Option, Signup,
                                Signin, Institution, UserAnswer, Event, SponsorEvent)


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

class SponsorEventAdmin(admin.ModelAdmin):
    # Display the event's name, sponsor name, donation amount, message, and creation time in the list view
    list_display = ('event_name', 'sponsor_name', 'donation_amount', 'message', 'created_at')

    # Filter by event and donation amount
    list_filter = ('event', 'donation_amount')

    # Enable search by sponsor name, sponsor email, and event name
    search_fields = ('sponsor_name', 'sponsor_email', 'event__name')  # 'event__name' allows searching by event name

    def event_name(self, obj):
        return obj.event.name  # Assumes your Event model has a 'name' field
    event_name.short_description = 'Event Name'  # Custom column name in the admin list view

    # Display the creation timestamp
    def created_at(self, obj):
        return obj.created_at  # Assumes your model has a 'created_at' field
    created_at.short_description = 'Created At'  # Custom column name for created_at field


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
admin.site.register(SponsorEvent, SponsorEventAdmin)