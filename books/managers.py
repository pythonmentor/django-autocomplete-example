from django.db import models


class BookManager(models.Manager):
    def get_all_by_term(self, term):
        return self.filter(title__icontains=term)
