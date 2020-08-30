from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
