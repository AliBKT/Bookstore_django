from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm, CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = "books/DeatailBook.html"
#     context_object_name = 'book'

def book_deatail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get cooments for book
    comments = book.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, "books/DeatailBook.html", {
        'book': book,
        'comments': comments,
        'comment_form': comment_form,
    })


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
