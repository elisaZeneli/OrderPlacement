from django import forms
from django.contrib.auth.models import User

from .models import Menu, Menu_Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name',)



class Menu_ItemForm(forms.ModelForm):
    class Meta:
        model = Menu_Item
        fields = ('name', 'price', 'description')