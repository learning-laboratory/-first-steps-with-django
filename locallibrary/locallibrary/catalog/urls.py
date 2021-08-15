from django.urls import path
from catalog.views import (
    index,
    BookListView,
    BookDetailView,
    AuthorListView,
    AuthorDetailView,
    LoanedBooksByUserListView
) 

urlpatterns = [
    path('',index, name='index'),
    path("books/", BookListView.as_view(), name="books"),
    path("books/<int:id>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="authors"),
    path("authors/<int:id>/", AuthorDetailView.as_view(), name="author-detail"),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]