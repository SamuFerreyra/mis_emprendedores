from django.db import models
from django.contrib.auth.models import User

class Emprendedor(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    telefono = models.CharField(
        max_length=20, 
        help_text="Ejemplo: 5491122334455 (Sin espacios ni el +)",
        null=True, 
        blank=True
    )
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
    vendedor = models.ForeignKey(Emprendedor, on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen_url = models.URLField(blank=True, help_text="URL opcional")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.vendedor.nombre_tienda}"

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes_extras', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/extras/')

    def __str__(self):
        return f"Imagen extra de {self.producto.nombre}"
    



class Servicio(models.Model):
    vendedor = models.ForeignKey(Emprendedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100) # Ej: Instalación de Aire
    categoria = models.CharField(max_length=100) # Ej: Refrigeración
    descripcion = models.TextField()
    activo = models.BooleanField(default=True) # Para que ellos lo apaguen/prendan
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)

    def __clase__(self):
        return f"{self.nombre} - {self.categoria}"