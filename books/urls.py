from django.urls import path
from django.views.generic import TemplateView
from .views import BookListView



urlpatterns = [
    path('', BookListView.as_view(template_name='books/book_inventory.html') , name='books-inventory')





]