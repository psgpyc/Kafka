from django.contrib import admin
from .models import Book, UserBooks
# Register your models here.
admin.site.register(Book)
admin.site.register(UserBooks)