from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    download_url = models.CharField(max_length=200)
    publication_year = models.IntegerField('year published', default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

