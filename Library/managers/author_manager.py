from django.db import models
from django.db.models import Count


class AuthorManager(models.Manager):
    def with_books_count(self):
        return super().get_queryset().annotate(books_count=Count('books'))
