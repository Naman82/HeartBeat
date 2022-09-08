from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_deliveryPerson = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_bloodbank = models.BooleanField(default=False)

class DeliveryPersonProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    profile_pic=models.ImageField(upload_to='delivery/profile/images', blank=True, null=True)
    address=models.TextField()
    city=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    pincode=models.CharField(max_length=10,null=True,blank=True)

class CustomerProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    profile_pic=models.ImageField(upload_to='profile/images', blank=True, null=True)
    address=models.TextField()
    city=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    pincode=models.CharField(max_length=10,null=True,blank=True)

class BloodStock(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    A_postive = models.IntegerField()
    A_negative = models.IntegerField()
    B_postive = models.IntegerField()
    B_negative = models.IntegerField()
    AB_postive = models.IntegerField()
    AB_negative = models.IntegerField()
    O_postive = models.IntegerField()
    O_negative = models.IntegerField()

class BloodBankProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blood_stock=models.ForeignKey(BloodStock,on_delete=models.CASCADE)
    address=models.TextField()
    city=models.CharField(max_length=100,blank=True)
    state=models.CharField(max_length=100,blank=True)
    pincode=models.CharField(max_length=10,blank=True)
    license_no=models.CharField(max_length=100,blank=True)
