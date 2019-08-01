from django.urls import path
from django.views.generic import TemplateView
from .views import BookListView
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', BookListView.as_view(template_name='books/book_inventory.html') , name='books-inventory'),
    path('add-book/<int:book_id>/<int:user_id>/', login_required(views.UserAddBooksView.as_view()),
         name='user_add_books'),
    path('favourite-book/<int:book_id>/<int:user_id>/', login_required(views.UserAddFavouriteBooksView.as_view()),
         name='user_add_favourite_books'),

]