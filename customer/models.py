from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    options = (
        ("incart","incart"),
        ("orderplaced","orderplaced"),
        ("cancelled","cancelled")
    )
    status = models.CharField(max_length=20,choices=options,default="incart")

