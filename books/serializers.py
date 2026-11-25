from rest_framework import serializers
from .models import BookInfo, BookFile

class BaseBookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = BookInfo
        fields = ['id', 'title', 'slug', 'authors', 'genres', 'cover', 'published', 'downloads']

class BookListSerializer(BaseBookSerializer):
    pass

class BookFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        fields = ['format', 'size', 'file']

class BookDetailSerializer(BaseBookSerializer):
    book_files = BookFileSerializer(many=True)

    class Meta(BaseBookSerializer.Meta):
        fields = BaseBookSerializer.Meta.fields + ['description', 'language', 'book_files']