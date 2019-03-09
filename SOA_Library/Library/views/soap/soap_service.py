import json
import base64

from django.views.decorators.csrf import csrf_exempt
from spyne import ComplexModel, String
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

from Library.helpers import to_dict
from Library.models.author import Author
from Library.models.book import Book
from Library.serializers.author import AuthorSerializer, AuthorDetailSerializer
from Library.serializers.book import BookSerializer, BookDetailSerializer


class SoapService(ServiceBase):
    @rpc(_returns=Unicode)
    def get_authors(ctx):
        queryset = Author.objects.all()
        ser = AuthorSerializer(queryset, many=True)
        return json.dumps(to_dict(ser.data))

    @rpc(Integer, _returns=Unicode)
    def get_author_by_id(ctx, id):
        queryset = Author.objects.with_books_count().get(pk=id)
        ser = AuthorDetailSerializer(queryset)
        return json.dumps(to_dict(ser.data))

    @rpc(_returns=Unicode)
    def get_books(ctx):
        queryset = Book.objects.all()
        ser = BookSerializer(queryset, many=True)
        return json.dumps(to_dict(ser.data))

    @rpc(Integer, _returns=Unicode)
    def get_book_by_id(ctx, id):
        queryset = Book.objects.get(pk=id)
        ser = BookDetailSerializer(queryset)
        ser._data['cover'] = ser.data['cover'].decode('utf8')
        return json.dumps(ser.data)


django_soap_application = DjangoApplication(Application(
    [SoapService],
    tns='django.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
))
soap_application = csrf_exempt(django_soap_application)
