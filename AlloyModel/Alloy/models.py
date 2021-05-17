from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class User_Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.TextField(max_length=100)
