from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.utils import timezone

# Create your views here.

def bookList(request):
    books = Book.objects.all()
    dictt = {'books': books}
    return render(request, 'board/book_list.html', dictt)

def bookDetail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    dictt = {'book': book}
    return render(request, 'board/book_detail.html', dictt)

@login_required(login_url="main:login")
def bookReview(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.create_date = timezone.now()
            review.book = book
            review.user = request.user
            review.save()
            return redirect('board:book_detail', book_id=book.id)
    else:
        form = BookReviewForm()
    dictt = {'book': book, 'form': form}
    return render(request, 'board/book_detail.html', dictt)