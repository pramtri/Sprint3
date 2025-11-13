from django.contrib import admin
from django.urls import path, include
from management import views as management_views # Importamos tus vistas de pedidos

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas para Auth0 (login/callback)
    path('', include('social_django.urls')),
    
    # Rutas de tu experimento (Pedidos)
    path('orders/', management_views.order_list, name='order_list'),
    path('orders/create/', management_views.order_create, name='order_create'),
    
    # Ruta para Logout
    path('logout/', include('django.contrib.auth.urls')),
]