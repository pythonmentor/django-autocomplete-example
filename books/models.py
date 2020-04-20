from django.db import models

from .managers import BookManager


class Book(models.Model):
    title = models.CharField("book title", max_length=150)

    objects = BookManager()

    def __str__(self):
        return self.title
