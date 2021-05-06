from django.db import models
from apps.core.models import DateTimeModel

# Create your models here.
class Product(DateTimeModel):
    name = models.CharField(max_length=150,blank=False,null=False)
    title = models.CharField(max_length=150,blank=False,null=False)
    price = models.DecimalField(default=0,blank=False,null=False,max_digits=3,decimal_places=2)
