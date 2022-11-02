from django.shortcuts import render
from django.views import generic


from .models import Book


class BookListView(generic.ListView):
    template_name = "books/book_list.html"
    model = Book
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/DeatailBook.html"
    context_object_name = 'book'

