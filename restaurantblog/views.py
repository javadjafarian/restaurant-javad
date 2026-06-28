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


   



