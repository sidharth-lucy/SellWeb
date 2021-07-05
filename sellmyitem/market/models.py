from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField

from auction.models import Flashsell
# Create your models here.

# class Postitem(models.Model):
#     # user= models.ForeignKey(User,related_name='post',on_delete=CASCADE)
    # flash= models.OneToOneField(Flashsell,related_name='flash',on_delete=CASCADE)
                            
#     about_product= models.CharField(max_length=500)
#     price= models.IntegerField()
#     product_img= models.ImageField()
#     product_tag= models.CharField(max_length=100)
#     contact= models.IntegerField(max_length=12,Required=False)




