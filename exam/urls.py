from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('written/', views.written, name='written'),
    path('practical/', views.practical, name='practical'),
]