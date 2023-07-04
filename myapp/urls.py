from django.urls import path
from .views import *

app_name = 'myapp'

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

    path('employees/<int:pk>/update/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDelete.as_view(), name='employee-delete'),
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>', EmployeeDetail.as_view(), name='employee-detail'),
    path('employees_form/', EmployeeCreate.as_view(), name='employee-create'),

]