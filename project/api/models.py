from django.db import models

# Create your models here.

# ? what are exactly models?

class CarInfo(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=20)
    transmission = models.CharField(max_length=20)
    mileage = models.PositiveIntegerField(help_text="Mileage in kilometers")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
