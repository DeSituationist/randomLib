from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookListSerializer
from .models import BookInfo

# Create your views here.
class BooksListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookListSerializer