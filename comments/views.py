from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView
from books.models import BookInfo
from .serializers import CommentSerializer
from .models import Comment

# Create your views here.
class CommentsListView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        book_slug = self.kwargs['book_slug']
        return Comment.objects.filter(book__slug=book_slug, visible=True).order_by('-published_at')

    def perform_create(self, serializer):
        book_slug = self.kwargs['book_slug']
        book = get_object_or_404(BookInfo, slug=book_slug)
        serializer.save(book=book)