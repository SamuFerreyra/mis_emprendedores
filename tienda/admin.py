from django.contrib import admin
from .models import Emprendedor, Producto, ImagenProducto

# 1. Configuración para las fotos extras
class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 3 # Muestra 3 espacios vacíos para subir fotos

# 2. Configuración para los Emprendedores
@admin.register(Emprendedor)
class EmprendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_tienda', 'rubro', 'usuario')
    
    # Filtra para que el emprendedor solo vea su propio perfil en el admin
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)

# 3. Configuración para los Productos (Aquí es donde estaba el lío)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]
    list_display = ['nombre', 'vendedor', 'precio']

    # FILTRO CLAVE: Solo permite que el emprendedor vea y edite SUS propios productos
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Filtramos los productos según el usuario logueado
        return qs.filter(vendedor__usuario=request.user)

    # ASIGNACIÓN AUTOMÁTICA: Al crear un producto, se le asigna la tienda del usuario actual
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            try:
                # Buscamos el perfil de emprendedor vinculado al usuario que está en el admin
                emprendedor = Emprendedor.objects.get(usuario=request.user)
                obj.vendedor = emprendedor
            except Emprendedor.DoesNotExist:
                pass 
        super().save_model(request, obj, form, change)