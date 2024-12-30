import uuid
from django.db import models

class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.DecimalField(max_digits=19, decimal_places=4, default=0)
