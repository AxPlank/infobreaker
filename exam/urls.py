from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('written/', views.written, name='written'),
    path('written/<int:part>', views.writtenPart, name='writtenPart'),
    path('practical/', views.practical, name='practical'),
    path('practical/<int:part>', views.practicalPart, name='practicalPart'),
]