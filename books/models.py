from django.db import models
import datetime



class Book(models.Model):
    title = models.CharField(max_length=100)
    descriprion = models.CharField(max_length=255, null=True)
    relase_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'

