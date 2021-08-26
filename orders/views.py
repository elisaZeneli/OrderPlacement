from django.shortcuts import render, redirect
from .models import Order, OrderImage, Person
from django.contrib.auth.models import Group, User
from menu.models import Menu_Item, Menu
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.timezone import datetime
from datetime import timedelta
from datetime import date



# Create your views here.

@login_required
@permission_required('orders.can_add_row', raise_exception=True)
@permission_required("orders.can_update_row", raise_exception=True)
def create_person(request):
    if request.method == 'POST':
        username = request.POST['username']
        daily_amount = request.POST['daily_amount']
        weekly_amount = request.POST['weekly_amount']

        try:
            Person.objects.filter(user = User.objects.get(username=username)).delete()
            p = Person(user=User.objects.get(username=username), daily_amount=daily_amount, weekly_amount=weekly_amount)
            p.save()
            messages.success(request, "Data is added successfully")  
            return render(request, 'orders/create_person.html')
        
        except:
            #Person.objects.create(user=User.objects.get(username=username), daily_amount=daily_amount, weekly_amount=weekly_amount)
            p = Person(user=User.objects.get(username=username), daily_amount=daily_amount, weekly_amount=weekly_amount)
            p.save()
            messages.success(request, "Data is added successfully")  
            return render(request, 'orders/create_person.html')
    else:
        
        return render(request, 'orders/create_person.html')



def place_order(request):
    if request.method == "POST":
        menu = Menu.objects.all()
        
        if (menu[0].date_created - timezone.now()).total_seconds() > 7200:
            messages.warning(request, "Orders are no longer taken.")
            return render(request, 'menu/menu.html' )
        
        meals_list = request.POST.getlist('meals')

        total = sum([Menu_Item.objects.get(id=meal_id).price for meal_id in meals_list])

        try:
            menu = Menu_Item.objects.get(id=meals_list[0]).menu
            
        except:

            return render(request, 'menu/menu.html' )
        try:
            person = Person.objects.get(user=request.user)
        
        except:

            messages.warning(request, "You cannot order now. Come later.")
            return render(request, 'menu/menu.html' )

        #ForeignKey option
        for meal_id in meals_list:
            meal = Menu_Item.objects.get(id=meal_id)
            
            if date.today().weekday() == 4 and person.weekly_amount > total:
                    person.daily_amount = person.weekly_amount
                    person.save()
                    

            if person.daily_amount < total:
                messages.warning(request, 'You have only : {}'.format(person.daily_amount))
                return render(request, 'menu/menu.html')



            order = Order(user=request.user, menu=menu, meal=meal, date=timezone.now())
            order.save()
            print(order.menu)
           
           
    

        person = Person.objects.get(user=request.user)
        person.daily_amount = person.daily_amount - total
        person.weekly_amount = person.weekly_amount - total
        person.save()
        
        messages.success(request, 'The order is placed.')
        
        return render(request, 'menu/menu.html', {'total': total})
        
        
        


@login_required
def check_orders(request):
    orders = Order.objects.filter(user=request.user).filter(date__lt=timezone.now()).order_by('-date')
    
    return render(request, 'orders/check_orders.html', {'orders': orders})



@login_required
@permission_required('orders.can_view_others_info', raise_exception=True)
def get_users_info(request):
    users = User.objects.filter(groups='1')
    return render(request, 'orders/users_info.html', {'users' : users})


@login_required
def get_user_info(request):
    try:

        person = Person.objects.get(user=User.objects.get(username=request.user))
        return render(request, "orders/user_info.html", {'person': person})

    except:
        messages.warning(request, "There is no information yet.")
        return render(request, "orders/user_info.html")


@login_required
@permission_required('orders.can_view_others_info', raise_exception=True)
def check_users_orders(request, pk):
    orders = Order.objects.filter(user=User.objects.get(username=pk))
    
    try:
        person = Person.objects.get(user=User.objects.get(username=pk))
        return render(request, 'orders/check_users_orders.html', {'orders' : orders, 'person': person})
    except:
        return render(request, 'orders/check_users_orders.html', {'orders' : orders})
    


@login_required
@permission_required('orders.can_view_others_info', raise_exception=True)
def check_daily_orders(request):
    orders = Order.objects.filter(date=datetime.today())
    
    return render(request, 'orders/daily_orders.html', {'orders': orders})


@login_required
@permission_required('orders.can_view_others_info', raise_exception=True)
def check_weekly_orders(request):
    orders = []
    for i in range(7):
        orders += Order.objects.filter(date=datetime.now() - timedelta(days=i))
    return render(request, 'orders/weekly_orders.html', {'orders': orders})


@login_required
def upload_image(request, pk):
    if request.method == 'POST' and 'image' in request.FILES:
        user = User.objects.get(username=pk)
        image = request.FILES['image']
        order_image = OrderImage(user=user, image=image, date=timezone.now())
        order_image.save()
    

    messages.success(request, "Image is uploaded. The order is being processed.")
    return render(request, 'menu/menu.html')


def delete_images():
    OrderImage.objects.all().delete()
    
