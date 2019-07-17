from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'books'


    def get_context_data(self, **kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context['title'] = 'Inventory'
        return context


