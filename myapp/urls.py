from django.urls import path
from .views import *

urlpatterns = [
    path('', index_myapp, name='index'),  # Путь "корень"
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('cars/<int:pk>/', car_card, name='car_card'),
    path('cars/', cars, name='cars'),
    path('drivers/<int:pk>/', driver_card, name='driver_card'),
    path('drivers/', drivers, name='drivers'),
    path('contacts/<str:id>/', contacts, name='contacts'),  # перед слешем долно быть цыфровое значение
    path('clients/<int:pk>/', client_card, name='client_card'),
    path('clients/', clients, name='clients'),
    path('add_car/', add_car, name='add_car'),
    path('add_driver/', add_driver, name='add_driver'),
    path('add_client/', add_client, name='add_client'),
]