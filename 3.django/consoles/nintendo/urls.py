from django.urls import path
from . import views

app_name = 'nintendo'

urlpatterns = [
    path('', views.view_inicio, name='inicio'),
    path('lancamentos/', views.view_lancamentos, name='lancamentos'),
    path('lancamentos/modelo/<str:link_url>/', views.view_modelo, name='modelo'),
]
