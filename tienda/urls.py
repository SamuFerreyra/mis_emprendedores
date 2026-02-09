from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('emprendedor/<int:pk>/', views.productos_emprendedor, name='productos_emprendedor'),
    # AGREGA ESTA LÍNEA:
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
]