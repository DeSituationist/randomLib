from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import BookListSerializer, BookDetailSerializer
from .models import BookInfo, BookFile
from ..comments.models import Comment
from ..api.pagination import StandardBookPagination

# Create your views here.
class BooksListView(ListAPIView):
    queryset = BookInfo.objects.filter(visible=True).prefetch_related('authors', 'genres')
    serializer_class = BookListSerializer
    pagination_class = StandardBookPagination

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'books/book_list.html'

    def get_queryset(self):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            return Response({'books': page, 'page_obj': page, 'paginator': self.paginator})

        return Response({'books': queryset})

class BookDetailView(RetrieveAPIView):
    queryset = BookFile.objects.filter(book_info__visible=True).prefetch_related('book_info')
    lookup_field = 'slug'
    serializer_class = BookDetailSerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'books/book_detail.html'

    def get(self, *args, **kwargs):
        book = self.get_object()
        comments = Comment.objects.filter(book=book, visible=True)

        return Response({'book': book, 'comments': comments})