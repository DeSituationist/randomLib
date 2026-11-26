from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register
class CommentAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'book', 'published_at', 'visible']
    list_editable = ['visible',]
    list_fitler = ['visible', 'nickname']
    search_fields = ['nickname', 'text', 'book__title']