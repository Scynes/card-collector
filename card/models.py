from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    card_type = models.CharField(max_length=20)
    description = models.TextField()
    value = models.IntegerField()
    card_image = models.CharField(default='none', max_length=255)