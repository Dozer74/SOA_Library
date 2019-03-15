from rest_framework import serializers
from Library.models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(read_only=True)
    biography = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class AuthorDetailSerializer(serializers.ModelSerializer):

    from Library.serializers.book import BookSerializer
    books = BookSerializer(many=True, read_only=True)
    biography = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Author
        fields = '__all__'
