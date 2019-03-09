import base64

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.fields import ImageField

from Library.models.author import Author
from Library.models.book import Book


class BookSerializer(serializers.ModelSerializer):
    authors_names = serializers.CharField(source='authors_short_names', read_only=True)
    authors_ids = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        many=True,
        source='authors',
        write_only=True)

    description = serializers.CharField(write_only=True, allow_blank=True, required=False)
    cover = Base64ImageField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = Book
        fields = ('id', 'authors_names', 'authors_ids', 'description', 'title', 'year', 'genre', 'cover')


class BookDetailSerializer(serializers.ModelSerializer):
    from Library.serializers.author import AuthorSerializer
    authors = AuthorSerializer(many=True, read_only=True)
    authors_ids = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        many=True,
        source='authors',
        write_only=True)

    cover = Base64ImageField(use_url=False, required=False, allow_null=True)

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # Converts image to base64
        if rep['cover'] is not None:
            with open(rep['cover'], 'rb') as img_file:
                rep['cover'] = base64.b64encode(img_file.read())
        return rep

    class Meta:
        model = Book
        fields = '__all__'
