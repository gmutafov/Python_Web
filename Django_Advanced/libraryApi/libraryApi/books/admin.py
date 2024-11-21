from django.contrib import admin
from unfold.admin import ModelAdmin

from libraryApi.books.models import Book


# Register your models here.


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
