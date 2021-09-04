from orders.models import DatabaseInfo
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from .models import Menu, Menu_Item
from django.contrib import messages

# Create your views here.


def main(request):
    db_info = DatabaseInfo.objects.all()[0]
    return render(request, 'menu/main.html', {'db_info': db_info})



def show_menu(request):
    meals = Menu_Item.objects.all()
    print(meals)
    return render(request, 'menu/menu.html', {'meals': meals})


@login_required
@permission_required('orders.can_add_row', raise_exception=True)
@permission_required("orders.can_update_row", raise_exception=True)
def create_menu(request):
    if request.method == 'POST':
        menu = Menu.objects.all()
        meal = request.POST['meal']
        price = request.POST['price']
        category = request.POST['category']
        description = request.POST['description']
            
        try:
            Menu_Item.objects.create(name=meal, price=price, description=description, menu=menu[0], meal_category=category)
            messages.success(request, "Meal entered successfully. Add another one.")
            return render(request, "menu/create_menu.html")
        
        except:
            menu_obj = Menu.objects.create(name=menu, date_created=timezone.now())
            Menu_Item.objects.create(name=meal, price=price, description=description, menu=menu[0], meal_category=category)
        
        messages.success(request, "Meal entered successfully. Add another one.")
        return render(request, 'menu/create_menu.html')
    
    else:
        return render(request, 'menu/create_menu.html')

