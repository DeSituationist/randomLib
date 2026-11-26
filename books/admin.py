from django.contrib import admin
from .models import Author, BookFile, BookInfo, Genre

# Register your models here.
class BookFileInLine(admin.TabularInline):
    model = BookFile
    extra = 1
    max_num = 2

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'language', 'visible', 'downloads']
    list_editable = ['visible',]
    list_filter = ['visible', 'genres', 'published']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ['title',]}

    inlines = [BookFileInLine]

@admin.register(Author, Genre)
class NameSlugAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name']