from django.shortcuts import render, get_object_or_404
from .models import Emprendedor, Producto

# Vista principal: muestra a los emprendedores
def home(request):
    emprendedores = Emprendedor.objects.all()
    return render(request, 'tienda/home.html', {'emprendedores': emprendedores})

# Vista de productos: muestra los productos de un emprendedor específico
def ver_productos(request, emprendedor_id):
    # Esto es mejor que .get() porque evita errores si el ID no existe
    emprendedor = get_object_or_404(Emprendedor, id=emprendedor_id) 
    productos = Producto.objects.filter(vendedor=emprendedor)
    return render(request, 'tienda/productos.html', {
        'emprendedor': emprendedor,
        'productos': productos
    })