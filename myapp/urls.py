from django.urls import path
from .views import about, login, contacts, index_myapp, drivers, cars

urlpatterns = [
    path('', index_myapp, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('contacts/<int:id>/', contacts, name='contacts'),
    #path('add_form/', add_form, name='add_form')
]