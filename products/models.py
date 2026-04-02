from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=50,unique=True)
    price = models.IntegerField()
    quantity = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images')
    bill = models.FileField(upload_to='bill/',null=True,blank=True)
    register_at = models.DateTimeField(auto_now_add=True)
