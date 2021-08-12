from django.contrib import admin

from books.models import Book

class CustomBookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'description', 'phone_number')




admin.site.register(Book, CustomBookAdmin)
