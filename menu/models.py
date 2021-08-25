from django.db import models
from django.utils import timezone

# Create your models here.


class Menu(models.Model):
    class Meta:
        
        permissions = (("can_add_row", "Can add new rows"),("can_update_row", "Can update rows"), ("can_delete_rows", "Can delete rows"))


    name = models.CharField(max_length=200, unique=True, blank=False, null=False, primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    
    
    def has_expired(self):
        return (self.date_created - timezone.now()).total_seconds() > 7200
    
    
    def __str__(self):
        return self.name




class Menu_Item(models.Model):
    class Meta:
        
        permissions = (("can_add_row", "Can add new rows"),("can_update_row", "Can update rows"), ("can_delete_rows", "Can delete rows"))

    CATEGORIES = [('main_course', 'Main Course'), ('drinks', 'Drinks'), ('starters', 'Starters')]

    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    menu = models.ForeignKey(Menu,  on_delete=models.SET_NULL, null=True, blank=True)
    
    meal_category = models.CharField(max_length=50, choices=CATEGORIES, null=True, blank=True)

    def change_price(self, price):
        self.price = price
        self.save()



    def __str__(self):
        return super().__str__()
