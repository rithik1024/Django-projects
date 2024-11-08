from django.db import models
# Create your models here.
class travels(models.Model):
    name=models.CharField(max_length=100)
    bus_no=models.IntegerField()
    start_point=models.CharField(max_length=100)
    end_point=models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    