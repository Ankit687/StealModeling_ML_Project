from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class User_Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.TextField(max_length=100)


class Metals_Composition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carbon = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    silicon = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    manganese = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    phosphorus = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    nickel = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    chromium = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    molybdenum = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    manganese_sulfur = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    cooling_rate = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    tempering_temperature = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    yield_strength = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    ultimate_tensile_strength = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    percentage_elongation = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    reduction_in_area = models.DecimalField(default=10, max_digits=5, decimal_places=3)
    impact_energy = models.DecimalField(default=10, max_digits=5, decimal_places=3)
