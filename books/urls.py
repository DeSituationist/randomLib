from django.urls import path
from .views import BooksListView, BookDetailView

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
]