from django.views.generic import ListView,DetailView
from .models import Food,FoodType,ContactUs,Order



class Home(ListView):
    model = Food
    template_name = 'index.html'
    context_object_name = 'foods'

class Detail(DetailView):
    model = Food
    template_name = 'detail.html'
    context_object_name = 'food'   

class Breakfast(Home):
    queryset = Food.objects.filter(food_types__title='صبحانه')
    template_name = 'breakfast.html'

class Lunch(Home):
    queryset = Food.objects.filter(food_types__title='ناهار')
    template_name = 'lunch.html'

class Dinner(Home):
    queryset = Food.objects.filter(food_types__title='شام')
    template_name = 'dinner.html'

class FastFood(Home):
    queryset = Food.objects.filter(food_types__title='فست‌فود')
    template_name = 'fast_food.html'

class Persian(Home):
    queryset = Food.objects.filter(food_types__title='ایرانی')
    template_name = 'persian.html'

class Drinks(Home):
    queryset = Food.objects.filter(food_types__title='نوشیدنی')
    template_name = 'drinks.html'

class Detail(DetailView):
    model = Food
    template_name = 'detail.html'
    context_object_name = 'food'   


   



