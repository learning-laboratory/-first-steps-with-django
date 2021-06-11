from django.shortcuts import render, get_object_or_404
from catalog.models import Book, Author, BookInstance, Genre, Language

from django.views.generic import (
    ListView,
    DetailView
) 

class AuthorListView(ListView):
    model = Author
    paginate_by = 2
    context_object_name = "authors"
    queryset = Author.objects.all()
    template_name = "authors/author_list.html"

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "authors/author_detail.html"

    def get_object(self):
        return get_object_or_404(Author, id=self.kwargs.get("id"))

class BookListView(ListView):
    model = Book
    paginate_by = 2
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'
    
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    
    def get_object(self):
        return get_object_or_404(Book, id=self.kwargs.get("id"))
    
def index(request):
    """View function for home page site"""

    # generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # the 'all()' is implied by default
    num_authors = Author.objects.count()
    
    num_genders = Genre.objects.count()
    num_languages = Language.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genders': num_genders,
        'num_languages': num_languages,
    }

    # render the HTML template index.html with the data n the context 
    return render(request, 'index.html', context=context)

