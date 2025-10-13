from django.db import models

# Create your models here.

# ? what are exactly models?

class Item(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)