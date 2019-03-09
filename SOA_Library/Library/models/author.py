from django.db import models

from Library.managers.author_manager import AuthorManager


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)
    year_birth = models.IntegerField()
    year_death = models.IntegerField(null=True, blank=True)

    objects = AuthorManager()

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
