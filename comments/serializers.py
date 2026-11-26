from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    book_title = serializers.StringRelatedField(source='book')
    book_slug = serializers.SlugRelatedField(source='book', slug_field='slug', read_only=True)

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'text', 'published_at', 'book_title', 'book_slug']
        extra_kwargs = {"email": {"write_only": True}}