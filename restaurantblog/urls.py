from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('breakfast/', views.Breakfast.as_view(), name='breakfast'),
    path('lunch/', views.Lunch.as_view(), name='lunch'),
    path('dinner/', views.Dinner.as_view(), name='dinner'),
    path('fastfood/', views.FastFood.as_view(), name='fastfood'),
    path('persianfood/', views.Persian.as_view(), name='persianfood'),
    path('drinks/', views.Drinks.as_view(), name='drinks'),
    # path('about-us/', views.AboutUs.as_view(), name='about-us'),
    # path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    # path('order/', views.OrderView.as_view(), name='order'),
]