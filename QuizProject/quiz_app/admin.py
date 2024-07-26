from django.contrib import admin
from quiz_app import models

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'question')
    search_fields = ('title', 'question')

admin.site.register(models.Quiz)
# Register your models here.
