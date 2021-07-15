from django.db import models
from django.contrib.auth.models import User
from menu.models import *
# Create your models here.



class Order(models.Model):
    class Meta:
        
        permissions = (("can_add_row", "Can add new rows"),("can_update_row", "Can update rows"), ("can_delete_rows", "Can delete rows"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    meal = models.ForeignKey(Menu_Item, on_delete=models.CASCADE, null=True)

    date = models.DateField()
    def __str__(self):
        return self.user.username + '-' + self.meal.name



class Person(models.Model):
    class Meta:
        
        permissions = (("can_add_row", "Can add new rows"),("can_update_row", "Can update rows"), ("can_delete_rows", "Can delete rows"), ("can_view_info", "Can view info"), ("can_view_others_info", "Can view others info"))


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_amount = models.FloatField()
    weekly_amount = models.FloatField()
    

    def __str__(self):
        return self.user.username



