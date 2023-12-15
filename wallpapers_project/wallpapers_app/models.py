from django.db import models
from django.utils import timezone

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class ScreenType (models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Wallpaper (models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(null=True, upload_to='wallpapers')
    published = models.BooleanField(default=False)

    # author = models.USER
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    screen_type = models.ForeignKey(ScreenType, on_delete=models.CASCADE)

    download_count = models.PositiveIntegerField(default=0, blank=False, null=False)

    def increment_download_count(self):
        """ Increments download_count of an instance by 1"""
        self.download_count += 1
    
    def __str__(self):
        return self.title