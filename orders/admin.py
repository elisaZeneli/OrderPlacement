from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(Person)
admin.site.register(OrderImage)
admin.site.register(DatabaseInfo)
admin.site.register(ImagesSize)