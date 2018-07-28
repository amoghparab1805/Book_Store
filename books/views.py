from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404


class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

class BookDelete(DeleteView):
    model = Book
    template_name = 'books/delete.html'

    def get_success_url(self):
        return reverse('books:index', kwargs={'pk': self.pk})

    def objectDelete(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()