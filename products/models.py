from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    likes = models.PositiveBigIntegerField(default=0)


class User(models.Model):
    pass
