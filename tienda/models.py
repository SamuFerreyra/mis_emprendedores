from django.db import models
from django.contrib.auth.models import User

class Emprendedor(models.Model):
    # Vinculamos al emprendedor con un usuario del sistema
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_tienda = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100, help_text="Ej: Productos Capilares o Zapatillas")
    slug = models.SlugField(unique=True, help_text="Ej: capilares o zapatillas")
    class Meta:
        verbose_name = "Emprendedor"
        verbose_name_plural = "Emprendedores"

    def __str__(self):
        return self.nombre_tienda

class Producto(models.Model):
    # Quién vende el producto
    vendedor = models.ForeignKey(Emprendedor, on_delete=models.CASCADE, related_name='productos')

    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen_url = models.URLField(blank=True, help_text="hola")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.vendedor.nombre_tienda}"