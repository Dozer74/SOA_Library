from django.db import models
from .author import Author


class Book(models.Model):
    BOOK_GENRES = (
        ('fiction', 'Fiction'),
        ('sci-fi', 'Science fiction'),
        ('classic', 'Classic literature'),
        ('romance', 'Romance'),
    )
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=20, choices=BOOK_GENRES)
    authors = models.ManyToManyField(Author, related_name='books')
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    @property
    def authors_short_names(self):
        authors_names = [a.short_name for a in self.authors.all()]
        return ", ".join(authors_names)

    def __str__(self):
        return f'{self.title} - {self.authors_short_names}'
