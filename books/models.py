from django.db import models




class Book(models.Model):
    title = models.CharField(max_length=100)
    descriprion = models.CharField(max_length=255, null=True)
    phone_number = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'

