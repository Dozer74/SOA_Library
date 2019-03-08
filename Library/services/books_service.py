import base64
from typing import List

from Library.models import Book


class BooksService:
    @staticmethod
    def get_books_brief() -> List[dict]:
        """
        Queries brief info about books: id, title, authors, genre and year
        """
        query = Book.objects \
            .values('id', 'title', 'genre', 'year')

        return list(query)

    @staticmethod
    def get_book_by_id(id: int) -> dict:

        # get entity
        book_entity = Book.objects.get(pk=id)

        # get authors' names
        authors = list(book_entity.authors.values('id', 'first_name', 'last_name'))

        # encode cover image as base64 string
        try:
            with open(book_entity.cover.path, 'rb') as img_file:
                cover = base64.b64encode(img_file.read())
        except ValueError:
            cover = None

        # format response dict
        book = {
            'id': book_entity.id,
            'title': book_entity.title,
            'genre': book_entity.genre,
            'year': book_entity.year,
            'description': book_entity.description,

            'authors': authors,
            'cover': cover
        }
        return book
