
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     image=models.ImageField(default='avatar.jpg',upload_to="profile_images")

     def __str__(self):
        return f'{self.user.username}'

class Movie(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

    title=models.CharField(max_length=200)
    actors=models.TextField()

    description=models.TextField()
    release_date=models.DateField()
    poster=models.ImageField(default='avatar.jpg',upload_to="static/images")
    trailer=models.TextField()
    created_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return self.title

   