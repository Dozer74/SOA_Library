from modernrpc.core import rpc_method

from Library.services.authors_service import AuthorsService
from Library.services.books_service import BooksService


@rpc_method
def get_authors():
    return AuthorsService.get_authors_brief()


@rpc_method
def get_author_by_id(id: int):
    return AuthorsService.get_author_by_id(id)


@rpc_method
def find_author_by_name(search_query: str):
    return AuthorsService.find_author_by_name(search_query)


@rpc_method
def get_books():
    return BooksService.get_books_brief()


@rpc_method
def get_book_by_id(id: int):
    return BooksService.get_book_by_id(id)
