from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    weapon = models.CharField(max_length=255)
    