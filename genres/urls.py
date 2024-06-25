from django.urls import path
from genres import views

urlpatterns = [
    path('add/', views.add_genre, name='add_genre'),
    path('remove/<genre_id>', views.remove_genre, name='remove_genre'),
    path('list/', views.list_genres, name='list_genres'),
]
