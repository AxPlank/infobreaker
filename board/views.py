from django.shortcuts import render
from .models import *

# Create your views here.

def bookList(request):
    books = Book.objects.order_by('id')
    dictt = {'books': books}
    return render(request, 'board/book_list.html', dictt)

def bookReview(request, book_id):
    book = Book.objects.filter(id=book_id)
    dictt = {'book': book}
    return render(request, 'board/book_review.html', dictt)