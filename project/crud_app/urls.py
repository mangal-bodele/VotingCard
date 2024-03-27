from django.urls import path
from .views import create_votingcard,show_votingcard,update_votingcard,delete_votingcard

urlpatterns = [
    path('create/',create_votingcard, name='create_url'),
    path('show/',show_votingcard, name='show_url'),
    path('update/<int:pk>/',update_votingcard, name='update_url'),
    path('delete/<int:pk>/',delete_votingcard, name='delete_url')
]