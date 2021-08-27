from django.db import models
from django.contrib.auth.models import User
from menu.models import *
from django.utils.timezone import datetime


# Create your models here.



"""class OrderAmount:
    meal = models.ForeignKey(Menu_Item, related_name="order_amounts", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name="order_amounts", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
"""

class Order(models.Model):
    class Meta:
        
        permissions = (("can_add_row", "Can add new rows"),("can_update_row", "Can update rows"), ("can_delete_rows", "Can delete rows"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    meal = models.ForeignKey(Menu_Item, on_delete=models.CASCADE, null=True)
    

    date = models.DateField()
    def __str__(self):
        return self.user.username




class Person(models.Model):
    class Meta:
        
        permissions = (("can_add_row", "Can add new rows"),("can_update_row", "Can update rows"), ("can_delete_rows", "Can delete rows"), ("can_view_info", "Can view info"), ("can_view_others_info", "Can view others info"))


    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    daily_amount = models.FloatField()
    weekly_amount = models.FloatField()
    

    def __str__(self):
        return self.user.username



class OrderImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
