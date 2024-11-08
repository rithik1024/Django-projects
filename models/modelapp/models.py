from django.db import models
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    location=models.CharField(max_length=100)
    def __str__(self) :
        return self.name
    
class Bike(models.Model):
    name=models.CharField(max_length=100)
    Engine_volume=models.IntegerField()
    torque=models.IntegerField()
    top_speed=models.IntegerField()
    milage=models.IntegerField()
    
    def __str__(self) :
        return self.name
