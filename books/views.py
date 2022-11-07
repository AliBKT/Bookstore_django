from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/DeatailBook.html"
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    # form_class is optional if fields be defined
    # form_class = BookForm
    fields = ['title', 'discription', 'author', 'price', 'cover']
    template_name = "books/add_book.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'discription', 'author', 'price', 'cover']
    template_name = "books/update_book.html"


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/delete_book.html"
    success_url = reverse_lazy('book_list')

