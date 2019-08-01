from django.db import models
from PIL import Image

from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=150)
    author_first_name = models.CharField(max_length=150)
    author_middle_name = models.CharField(max_length=150, blank=True, null=True)
    author_last_name = models.CharField(max_length=150)
    genre = models.CharField(max_length=50, blank=False)
    category = models.CharField(max_length=50, blank=False)
    language = models.CharField(max_length=10, blank=False)
    year = models.DateField()
    image = models.ImageField(upload_to='book_thumbnail')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def author_full_name(self):
        if self.author_middle_name:
            return "{} {} {}".format(self.author_first_name, self.author_middle_name, self.author_last_name)
        else:
            return "{} {}".format(self.author_first_name, self.author_last_name)


class UserBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, unique=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    is_Favorite = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.book.title)