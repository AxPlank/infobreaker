from django.db import models
from main.forms import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='board/bookcover/')
    price = models.IntegerField()
    publisher = models.CharField(max_length=255)
    stat_sum = models.IntegerField()
    cnt = models.IntegerField()
    stat_avg = models.FloatField()

    def __str__(self):
        return self.title

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stat = models.IntegerField()
    review = models.TextField()
    create_date = models.DateField()