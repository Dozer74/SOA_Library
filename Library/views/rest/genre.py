from django.http import JsonResponse
from rest_framework.views import APIView

from Library.models.book import Book


class GenreList(APIView):

    def get(self, request, format=None):
        res = []
        for genre, title in Book.BOOK_GENRES:
            res.append({
                'genre': genre,
                'full_title': title
            })
        return JsonResponse(res, safe=False)
