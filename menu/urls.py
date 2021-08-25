from django.urls import path
from . import views
from orders import views as order_views

urlpatterns = [
    path('', views.main, name='main'),
    path('menu/', views.show_menu, name='menu'),
    #path('menus/<str:pk>/', views.show_menu, name='show_menu'),
    path('create_menu/', views.create_menu, name='create_menu'),

]