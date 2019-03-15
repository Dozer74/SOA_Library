from rest_framework import generics

from Library.models.author import Author
from Library.serializers.author import AuthorSerializer, AuthorDetailSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects \
        .with_books_count() \
        .all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
