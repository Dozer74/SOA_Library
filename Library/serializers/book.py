import base64

from rest_framework import serializers
from rest_framework.fields import ImageField

from Library.models.author import Author
from Library.models.book import Book


class BookSerializer(serializers.ModelSerializer):
    authors_names = serializers.CharField(source='authors_short_names', read_only=True)

    authors = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Author.objects.all())
    description = serializers.CharField(write_only=True, required=False)
    cover = ImageField(write_only=True, required=False)

    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):

    from Library.serializers.author import AuthorSerializer
    authors = AuthorSerializer(many=True, read_only=True)

    cover = ImageField(use_url=False)

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
