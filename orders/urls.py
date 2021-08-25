from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('daily_orders/', views.check_daily_orders, name='daily_orders'),
    path('weekly_orders/', views.check_weekly_orders, name='weekly_orders'),
    path('create_person/', views.create_person, name='create_person'),
    path('place_order/', views.place_order, name='place_order'),
    path('previous_orders/', views.check_orders, name='check_previous_orders'),
    path('users_info/', views.get_users_info, name='users_info'),
    path('user_info/', views.get_user_info, name="user_info"),
    path('all_users_orders/<str:pk>/', views.check_users_orders, name='check_users_orders'),
    path('upload_image/<str:pk>/', views.upload_image, name='upload_image')
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
