from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return f'{self.author} : {self.title}'

    def get_absolute_url(self):
        return reverse('book_deatail', args=[self.id])

