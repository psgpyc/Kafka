from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Book
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User

from django.urls import reverse_lazy

from books.models import UserBooks
from books.models import Book


class BookListView(ListView):
    context_object_name = 'books'

    def get_queryset(self):
        userbooks = UserBooks.objects.all().values_list('book', flat=True)
        qs = Book.objects.exclude(pk__in=userbooks)
        return qs

    def get_context_data(self, **kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context['title'] = 'Inventory'
        context['select_books'] = UserBooks.objects.all()



        return context


class UserAddBooksView(TemplateView):
    template_name = 'books/book_inventory.html'

    def post(self, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['user_id'])
        book = Book.objects.get(pk=self.kwargs['book_id'])
        UserBooks.objects.create(book=book, profile=user)

        return HttpResponseRedirect(reverse_lazy('books-inventory'))


class UserAddFavouriteBooksView(TemplateView):
    template_name = 'books/book_inventory.html'

    def post(self, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['user_id'])
        book = Book.objects.get(pk=self.kwargs['book_id'])
        UserBooks.objects.create(book=book, profile=user, is_Favorite=True)

        return HttpResponseRedirect(reverse_lazy('books-inventory'))
