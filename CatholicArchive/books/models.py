from django.db import models
from django.utils import timezone

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    download_url = models.CharField(max_length=200)
    publication_year = models.IntegerField('year published', default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

