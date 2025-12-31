from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/emprunt/', views.api_emprunt, name='api_emprunt'),
    path('api/retour/', views.api_retour, name='api_retour'),
]