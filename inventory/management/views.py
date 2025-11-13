from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Order
from provesi.auth0backend import getRole # Importamos la función auxiliar [cite: 532]
from django.utils import timezone

@login_required
def order_list(request):
    orders = Order.objects.all()
    # Obtenemos el rol para mostrarlo en el frontend
    role = getRole(request) 
    return render(request, 'order_list.html', {'orders': orders, 'role': role})

@login_required
def order_create(request):
    role = getRole(request)
    
    # --- PUNTO DE CONTROL DE SEGURIDAD (ASR) ---
    # Solo el Admin puede crear/modificar. El "Operario" (Hacker) será rechazado.
    if role != 'Admin': 
        return HttpResponseForbidden("403 Forbidden: No tienes permisos para manipular pedidos.")
    # -------------------------------------------

    if request.method == 'POST':
        # Lógica simple para crear pedido
        products_str = request.POST.get('products', '[]')
        count = request.POST.get('count', 0)
        Order.objects.create(
            products=products_str, 
            product_count=count,
            shipping_date=timezone.now()
        )
        return redirect('order_list')
    
    return render(request, 'order_form.html')