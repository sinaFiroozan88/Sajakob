from django.urls import path

from publishers import views

urlpatterns = [
    path('add/', views.add_publisher, name='add_publisher'),
    path('remove/<publisher_id>', views.remove_publisher, name='remove_publisher'),
    path('list/', views.list_publishers, name='list_publishers'),
]
