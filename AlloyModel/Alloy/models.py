from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class User_Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.TextField(max_length=100)


class Metals_Composition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carbon = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    silicon = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    manganese = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    phosphorus = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    nickel = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    chromium = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    molybdenum = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    sulfur = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    cooling_rate = models.DecimalField(default=10, max_digits=5, decimal_places=2)
    tempering_temperature = models.DecimalField(default=10, max_digits=5, decimal_places=2)
