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


def detalle_producto(request, pk):
    # Buscamos el producto por su ID (pk)
    producto = get_object_or_404(Producto, pk=pk)
    
    # Sugerencias: buscamos productos del mismo vendedor pero que no sean el actual
    sugerencias = Producto.objects.filter(vendedor=producto.vendedor).exclude(pk=pk)[:4]
    
    return render(request, 'tienda/detalle_producto.html', {
        'producto': producto,
        'sugerencias': sugerencias
    })


 
# Asegúrate de que el nombre sea exactamente este:
def productos_emprendedor(request, pk):
    emprendedor = get_object_or_404(Emprendedor, pk=pk)
    productos = Producto.objects.filter(vendedor=emprendedor)
    return render(request, 'tienda/productos.html', {
        'emprendedor': emprendedor,
        'productos': productos
    })