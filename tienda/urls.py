from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('emprendedor/<int:emprendedor_id>/', views.ver_productos, name='ver_productos'),
]