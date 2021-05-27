from django.urls import path
from catalog.views import (
    index,
    BookListView,
    BookDetailView,
) 

urlpatterns = [
    path('',index, name='index'),
    path("books/", BookListView.as_view(), name="books"),
    path("books/<int:id>/", BookDetailView.as_view(), name="book-detail")
]