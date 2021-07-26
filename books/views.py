from django.shortcuts import render
from rest_framework import viewsets

from books.models import Book
from books.serializers import Bookserializer


class BooksView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer