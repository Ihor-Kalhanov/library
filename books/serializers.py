from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from accounts.serializers import UserSerializer
from books.models import Book



class Bookserializer(ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True,)

    class Meta:
        model = Book
        fields = ("id", "title", "owner", "description", "phone_number", "created_at", "updated_at")


    def to_representation(self, instance):
        self.fields['owner'] = UserSerializer(read_only=True)
        return super(Bookserializer, self).to_representation(instance)
