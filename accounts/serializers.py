from rest_framework import serializers

from django.db import transaction


from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
