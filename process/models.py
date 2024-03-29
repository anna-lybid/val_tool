from django.db import models


class Bus(models.Model):
    info = models.CharField(max_length=255, null=True)
    num_seat = models.IntegerField()

    class Meta:
        verbose_name_plural = "buses"

    def __str__(self):
        return str(self.info)


class Product(models.Model):
    info = models.CharField(max_length=255, null=True)
    formula = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.info)
