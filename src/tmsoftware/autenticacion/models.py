from django.db import models
from django.contrib.auth.models import User

class Ingeniero(models.Model):
    ingeniero = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre 