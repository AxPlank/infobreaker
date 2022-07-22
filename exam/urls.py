from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('part', views.partChoice, name='part'),
    path('written/<int:part>', views.writtenPart, name='writtenPart'),
    path('practical/<int:part>', views.practicalPart, name='practicalPart'),
    path('problem/<int:problem_id>', views.problem, name='problem'),
    path('problem/<int:problem_id>/comment', views.comment, name='comment'),
    path('CBT', views.CBTChoice, name='CBT'),
    path('CBT/part/<int:part>', views.CBT_part, name='CBT_parttest'),
]