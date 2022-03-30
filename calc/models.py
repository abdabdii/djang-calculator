from statistics import mode
from django.db import models

# Create your models here.

class Operation(models.Model):
    name = models.CharField(max_length=12)
    symbol = models.CharField(max_length=3)

    def __str__(self):
        return f"({self.symbol}) - {self.name}"

class Calculation(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    operation = models.ForeignKey(Operation,on_delete=models.CASCADE)
    result = models.FloatField()

    def __str__(self):
        return "= %s" % self.result

