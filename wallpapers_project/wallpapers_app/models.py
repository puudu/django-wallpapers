from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
    def wallpaper_count(self):
        return self.wallpaper_set.count()

class ScreenType (models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Wallpaper (models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(null=True, upload_to='wallpapers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    screen_type = models.ForeignKey(ScreenType, on_delete=models.CASCADE)

    download_count = models.PositiveIntegerField(default=0, blank=False, null=False)

    def increment_download_count(self):
        """ Increments download_count of an instance by 1"""
        self.download_count += 1
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    wallpaper = models.ForeignKey(Wallpaper, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)