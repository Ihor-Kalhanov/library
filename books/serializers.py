from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
import datetime

from books.models import Book



class Bookserializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
