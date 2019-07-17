from django.db import models
from PIL import Image

class Book(models.Model):
    title = models.CharField(max_length=150 , blank=False)
    author_first_name = models.CharField(max_length=150, blank=False)
    author_middle_name = models.CharField(max_length=150, default="")
    author_last_name = models.CharField(max_length=150, default='')
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