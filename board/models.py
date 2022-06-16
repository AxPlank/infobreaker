from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='cover/')
    price = models.IntegerField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()