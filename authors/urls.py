from django.urls import path
from authors import views

urlpatterns = [
    path('add/', views.add_author, name='add_author'),
    path('remove/<author_id>', views.remove_author, name='remove_author'),
    path('list/', views.list_author, name='list_authors'),
]
