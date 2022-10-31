from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

