from django.urls import path, include
from . import views

app_name = 'lojinha'

urlpatterns = [
    path('', views.view_index, name='inicio'),
    path('search/', views.view_search, name='busca'),
]

