from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic import UpdateView
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

class BookUpdate(UpdateView):
    model = Book
    template_name = 'books/edit.html'

    def get_success_url(self):
        return reverse('books:index')

class BookDelete(DeleteView):
    model = Book
    template_name = 'books/delete.html'

    def get_success_url(self):
        return reverse('books:index')