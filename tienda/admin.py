from django.contrib import admin
from .models import Emprendedor, Producto

@admin.register(Emprendedor)
class EmprendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_tienda', 'rubro', 'usuario')
    
    # Esto hace que si no eres superusuario, no puedas ver la lista de otros emprendedores
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'vendedor', 'precio', 'stock')
    list_filter = ('vendedor',)

    # ¡ESTO ES LO CLAVE! 
    # Solo permite que el emprendedor vea y edite SUS propios productos
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Filtramos para que solo vea productos donde el vendedor es SU usuario
        return qs.filter(vendedor__usuario=request.user)

    # Esto hace que al crear un producto nuevo, se le asigne su tienda automáticamente
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            emprendedor = Emprendedor.objects.get(usuario=request.user)
            obj.vendedor = emprendedor
        super().save_model(request, obj, form, change)