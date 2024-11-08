from django.db import models

# Create your models here.

class media(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="image")
    video=models.FileField(upload_to='video')
    def __str__(self):
        return self.name