from django.db import models
from django.utils import timezone

# Create your models here.

'''
class Menu(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    
    def has_experied(self):
        return (self.date_created - timezone.now()).total_seconds() < 7200
    
    
    def __str__(self):
        return self.name




class Menu_Item(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    menu = models.ForeignKey(Menu,  on_delete=models.SET_NULL, null=True, blank=True)

    def change_price(self, price):
        self.price = price
        self.save()



    def __str__(self):
        return super().__str__()
'''