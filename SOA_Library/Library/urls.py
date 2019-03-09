from django.contrib import admin
from django.urls import path
from modernrpc.views import RPCEntryPoint
from Library.views.soap.soap_service import soap_application

from Library.models.author import Author
from Library.models.book import Book
from Library.views.rest.author import AuthorList, AuthorDetail
from Library.views.rest.book import BookList, BookDetail
from Library.views.rest.genre import GenreList

admin.site.register(Author)
admin.site.register(Book)

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'rpc/', RPCEntryPoint.as_view()),
    path(r'soap/', soap_application),

    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),

    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),

    path('genres/', GenreList.as_view())
]
