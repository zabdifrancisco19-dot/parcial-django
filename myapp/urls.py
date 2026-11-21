from django.urls import path
from . import views

urlpatterns = [
    path('programas/crear/', views.crear_programa, name='crear_programa'),
]