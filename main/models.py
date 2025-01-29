from django.db import models
from django.utils import timezone

CONDITION_CHOICES = {
    "new": "New",
    "used_like_new": "Used, like new",
    "used": "Used",
    "torn": "Torn",
}
class HardwareType(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hardware_types/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    brand = models.CharField(max_length=100,default='N/A')
    image_reverse = models.ImageField(upload_to='products/', blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    hardware_type = models.ForeignKey(HardwareType,on_delete=models.SET_NULL,related_name="products",blank=True,null=True)
    condition = models.CharField(max_length=50,choices=CONDITION_CHOICES,default="new")

    def __str__(self):
        return self.name
    
    def recently_published(self):
        return self.create_date >= timezone.now() - timezone.timedelta(days=7)
    
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name
    
