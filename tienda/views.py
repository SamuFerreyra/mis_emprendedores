from django.shortcuts import render, get_object_or_404
from .models import Emprendedor, Producto, Servicio

def home(request):
    emprendedores = Emprendedor.objects.all()
    return render(request, 'tienda/home.html', {'emprendedores': emprendedores})

def productos_emprendedor(request, pk):
    emprendedor = get_object_or_404(Emprendedor, pk=pk)
    es_servicio = (emprendedor.rubro == "Servicios Y Mantenimiento")
    
    # AGREGADO: Capturamos la profesión (categoría) de la URL si existe
    profesion_elegida = request.GET.get('profesion')

    if es_servicio:
        items = Servicio.objects.filter(vendedor=emprendedor)
        # MODIFICADO: Si el usuario hizo clic en una profesión, filtramos
        if profesion_elegida:
            items = items.filter(categoria__icontains=profesion_elegida)
    else:
        items = Producto.objects.filter(vendedor=emprendedor)

    return render(request, 'tienda/productos.html', {
        'emprendedor': emprendedor,
        'productos': items, 
        'es_servicio': es_servicio,
        'profesion_actual': profesion_elegida # Enviamos cuál está seleccionada
    })

def detalle_producto(request, pk):
    es_servicio = False
    try:
        item = get_object_or_404(Producto, pk=pk)
    except:
        item = get_object_or_404(Servicio, pk=pk)
        es_servicio = True
    
    if es_servicio:
        sugerencias = Servicio.objects.filter(vendedor=item.vendedor).exclude(pk=pk)[:4]
    else:
        sugerencias = Producto.objects.filter(vendedor=item.vendedor).exclude(pk=pk)[:4]
    
    return render(request, 'tienda/detalle_producto.html', {
        'producto': item,
        'sugerencias': sugerencias,
        'es_servicio': es_servicio
    })