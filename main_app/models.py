from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    release_year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.manufacturer} {self.name}"

class Game(models.Model):
    title = models.CharField(max_length=100)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.system})"

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} for {self.system}"
