import collections

from modernrpc.core import rpc_method

from Library.helpers import to_dict
from Library.models.author import Author
from Library.models.book import Book
from Library.serializers.author import AuthorSerializer, AuthorDetailSerializer
from Library.serializers.book import BookSerializer, BookDetailSerializer


@rpc_method()
def get_authors():
    queryset = Author.objects.all()
    ser = AuthorSerializer(queryset, many=True)
    return to_dict(ser.data)


@rpc_method
def get_author_by_id(id):
    queryset = Author.objects.with_books_count().get(pk=id)
    ser = AuthorDetailSerializer(queryset)
    return to_dict(ser.data)


@rpc_method
def get_books():
    queryset = Book.objects.all()
    ser = BookSerializer(queryset, many=True)
    return to_dict(ser.data)


@rpc_method
def get_book_by_id(id):
    queryset = Book.objects.get(pk=id)
    ser = BookDetailSerializer(queryset)
    return to_dict(ser.data)
