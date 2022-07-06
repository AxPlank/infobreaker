from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('review/', views.bookList, name='book_list'),
    path('review/<int:book_id>', views.bookReview, name='book_detail'),
    path('review/create/<int:book_id>', views.bookReview, name='book_review'),
]
