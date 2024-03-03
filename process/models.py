from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Enter goal description here")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, default="Default Product Name")
    description = models.TextField(default="Enter product description here")
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    contract_number = models.CharField(max_length=100)
    financed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField()
    balloon = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    annual_irr = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.contract_number


