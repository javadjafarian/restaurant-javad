from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(), name='home'),
    path('breakfast/',views.Brakefast.as_view(), name='breakfast'),
    path('dinner/',views.Brakefast.as_view(), name='dinner'),
    path('lunch/',views.Brakefast.as_view(), name='lunch'),
    path('drinks/',views.Brakefast.as_view(), name='drinks'),
    path('fastfood/',views.Brakefast.as_view(), name='fastfood'),
    path('persianfood/',views.Brakefast.as_view(), name='persianfood'),
    path('about-us/',views.Brakefast.as_view(), name='about-us'),
    path('contact-us/',views.Brakefast.as_view(), name='contact-us'),
]