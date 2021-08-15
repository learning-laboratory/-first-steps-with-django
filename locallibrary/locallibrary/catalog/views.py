from django.shortcuts import render, get_object_or_404
from catalog.models import Book, Author, BookInstance, Genre, Language
from django.views.generic import (
    ListView,
    DetailView
) 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genders': num_genders,
        'num_languages': num_languages,
        'num_visits': num_visits
    }

    # render the HTML template index.html with the data n the context 
    return render(request, 'index.html', context=context)


# @permission_required('catalog.can_mark_returned')
# @permission_required('catalog.can_edit')
class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing books on loan to current user."""
    permission_required = 'catalog.can_mark_returned'
    # Or multiple permissions
    # permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    # Note that 'catalog.can_edit' is just an example
    # the catalog application doesn't have such permission!
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')