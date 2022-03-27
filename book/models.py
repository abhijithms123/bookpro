from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=120, unique=True)
    Author = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.book_name


