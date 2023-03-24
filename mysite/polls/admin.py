from django.contrib import admin

from .models import Question, Choice

class QuestionChoiceInline(admin.TabularInline):
	model = Choice
	readonly_fields = ('id',)
	extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	inlines = [QuestionChoiceInline]