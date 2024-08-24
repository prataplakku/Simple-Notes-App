
from django.urls import path
from .views import register, login, add_note

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add_note/', add_note, name='add_note'),
]