from django.db import models

# Create your models here.


class Flashsell(models.Model):
    sellbool =models.BooleanField(default=False)
    start_price= models.IntegerField(null=True)
    end_datetime= models.DateTimeField(null=True)