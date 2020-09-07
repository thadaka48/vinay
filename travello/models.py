from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    offer= models.BooleanField(default=False)
    descr=models.TextField()
    img= models.ImageField(upload_to='pics')
    price=models.IntegerField()