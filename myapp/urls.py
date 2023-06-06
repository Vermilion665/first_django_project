from django.urls import path
from .views import about, login, contacts, index_myapp

urlpatterns = [
    path('', index_myapp),
    path('about/', about),
    path('login/', login),
    path('contacts/<int:id>/', contacts),
    #path('add_form/', add_form, name='add_form')
]