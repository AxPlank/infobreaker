from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'

urlpatterns = [
    path('', mainpage, name='main'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]
