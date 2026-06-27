from django.shortcuts import render
from django.views.generic import ListView
from .models import Food,FoodType,ContactUs,Order



class Home(ListView):
    model = Food
    template_name = 'index.html'
    context_object_name = 'foods'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_types'] = FoodType.objects.all()
        return context  

   



