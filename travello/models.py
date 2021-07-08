from django.db import models


# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    des = models.TextField()
    offer = models.BooleanField(default=False )
