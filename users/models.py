from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):

    def user_dir_path(self,filename):


        return 'profile_pics/user_{0}_{1}/{2}'.format(self.user.username,self.user.id,filename)



    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg',upload_to=user_dir_path)
    address = models.CharField(max_length=150,blank=False, default='Nepal')
    designation = models.CharField(max_length=150, blank=False, default='Member')
    phone = models.IntegerField(default=9876543210)



    def __str__(self):
        return self.user.username






    def save(self, *args, **kwargs):
        super().save(*args , **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



