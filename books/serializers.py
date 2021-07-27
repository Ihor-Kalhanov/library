from rest_framework import serializers
from rest_framework.fields import SlugField
from rest_framework.serializers import ModelSerializer
import datetime

from books.models import Book
from rest_framework.validators import UniqueValidator


class Bookserializer(ModelSerializer):
    relase_date = serializers.DateTimeField(format="%Y-%m-%d:%H:%M%S")

    def validate(self, data):
        if data['relase_date'] > datetime.date.today():
            raise serializers.ValidationError({
                "relase_date": "The date cannot be in the past!"
            })
        return data

    class Meta:
        model = Book
        fields = ('title', 'descriprion', 'relase_date', 'created_at', 'updated_at',)
