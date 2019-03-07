from django.db import models
from enum import Enum


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)
    year_birth = models.IntegerField()
    year_death = models.IntegerField(null=True, blank=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def short_name(self):
        return self.first_name[0] + '. ' + self.last_name

    @property
    def years_of_life(self):
        res = str(self.year_birth)
        if self.year_death is not None:
            res += ' - ' + str(self.year_death)
        return res

    def __str__(self):
        return f'{self.full_name} ({self.years_of_life})'


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

    def __str__(self):
        authors_names = [a.short_name for a in self.authors.all()]
        return f'{self.title} - {", ".join(authors_names)}'
