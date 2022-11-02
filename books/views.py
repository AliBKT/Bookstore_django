from django.shortcuts import render
from django.views import generic


from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    template_name = "books/book_list.html"
    model = Book
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/DeatailBook.html"
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    # form_class is optional if fields be defined
    # form_class = BookForm
    fields = ['title', 'discription', 'author', 'price']
    template_name = "books/add_book.html"

