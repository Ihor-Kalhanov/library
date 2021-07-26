from django.contrib import admin

from books.models import Book
from django.contrib.auth.admin import UserAdmin

class CustomBookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title','descriprion', 'relase_date')




admin.site.register(Book, CustomBookAdmin)
