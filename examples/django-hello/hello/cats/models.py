from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField()
