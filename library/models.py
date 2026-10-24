from django.db import models

# Create your models here.

class Book (models.Model):
    title = models.CharField(max_length=200 , null=False)
    author = models.CharField(max_length=200 , null=False)
    isbn = models.CharField(max_length=13 , unique=True)
    published_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


