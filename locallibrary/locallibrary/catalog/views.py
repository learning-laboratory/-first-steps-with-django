from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre, Language

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

