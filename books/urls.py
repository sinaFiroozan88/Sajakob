from django.urls import path
from books import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('remove/<book_id>', views.remove_book, name='remove_book'),
    path('list/', views.list_books, name='list_genres'),
]
