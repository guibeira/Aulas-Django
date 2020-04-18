from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    super_power = models.CharField(max_length=30)
