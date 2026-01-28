from django.db import models

# Create your models here.
class Head(models.Model):
    animal = models.CharField(max_length=64)
    price_per_kilo = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.FloatField()
    age = models.IntegerField()
    ready_for_sale = models.BooleanField(default=False)
    

    def __str__(self):
        return f'Animal: {self.animal}, Weight: {self.weight}, Age: {self.age}, $/kg: {self.price_per_kilo}, Ready for sale: {self.ready_for_sale}'