from django.urls import path
from .views import CommentsListView

urlpatterns = [
    path('books/<slug:book_slug>/comments/', CommentsListView.as_view(), name='book_comments'),
]