import datetime

from django.contrib.auth import get_user_model
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True)
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
