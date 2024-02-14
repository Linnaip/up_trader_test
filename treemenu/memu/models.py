from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
