from django.contrib import admin
from .models import Book, Genre, Author


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'id']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'author', 'genre']


admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
