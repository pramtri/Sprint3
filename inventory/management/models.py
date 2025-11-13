from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('TRANSITO', 'En Tránsito'),
        ('ALISTAMIENTO', 'En Alistamiento'),
        ('DESPACHADO', 'Despachado'),
    ]

    id = models.AutoField(primary_key=True)
    
    products = models.JSONField(default=list) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TRANSITO')
    creation_date = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateTimeField(null=True, blank=True)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Pedido {self.id} - {self.status}"