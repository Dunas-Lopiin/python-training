from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    published_date = models.DateField(null=True)

    character = models.OneToOneField('characters.Character', on_delete=models.CASCADE)

    

