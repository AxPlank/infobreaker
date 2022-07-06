from django import forms
from .models import *

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('stat', 'review')
        labels = {
            'stat': '평점',
            'review': '리뷰',
        }