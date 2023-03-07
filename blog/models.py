from django.db import models

class posts(models.Model):
    post_name = models.CharField(max_length=255)
    
