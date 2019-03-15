from typing import List
from django.db.models import Count, Value
from django.db.models.functions import Concat
from django.forms.models import model_to_dict

from Library.models import Author


class AuthorsService:
    @staticmethod
    def get_authors_brief() -> List[dict]:
        """
        Queries brief info about authors: id, name, years of life, books count
        """
        query = Author.objects \
            .annotate(num_book=Count('books')) \
            .values('id', 'first_name', 'last_name', 'year_birth', 'year_death', 'num_book')

        return list(query)

    @staticmethod
    def get_author_by_id(id: int) -> dict:
        """
        Queries author's full info with brief info about his books
        :param id: Author's id
        """
        author = Author.objects \
            .prefetch_related('books') \
            .get(pk=id)
        books = list(author.books.values('title', 'year', 'genre'))

        data = model_to_dict(author)
        data['books'] = books
        return data

    @staticmethod
    def find_author_by_name(search_query):
        queryset = Author.objects.annotate(a_full_name=Concat('first_name', Value(' '), 'last_name'))
        queryset = queryset.filter(a_full_name__icontains=search_query)
        queryset = queryset.values('id', 'first_name', 'last_name', 'year_birth', 'year_death')

        return list(queryset)
