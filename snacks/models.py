from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Snacks(models.Model):
    name = models.CharField(max_length=64)
    descripiton = models.TextField()
    purchaser = models.ForeignKey('auth.User', on_delete= models.CASCADE)

    def __str__(self):
        return self.name