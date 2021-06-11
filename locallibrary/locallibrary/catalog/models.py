from django.db import models
import uuid
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000,null=True, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',null=True, max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    language = models.ForeignKey('language', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={ 'id': str(self.id) })
    

class BookInstance(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library') 
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices = LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability'
    )

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth =  models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['first_name']
    
    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name