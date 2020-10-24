from django.contrib import admin

# Register your models here.

from .models import Question, Choice, Boxer

admin.site.site_header = "Pollster Admin X-Hunter"
admin.site.site_title = "Pollster Title Kilwa"
admin.site.index_title = "Welcome to X-Hunter Team"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, 
        {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Boxer)
