from django.views.generic import ListView,DetailView,TemplateView,FormView
from .models import Food,ContactUs,Order
from .forms import ContactUsForm


class Home(ListView):
    model = Food
    template_name = 'index.html'
    context_object_name = 'foods'

class Detail(DetailView):
    model = Food
    template_name = 'detail.html'
    context_object_name = 'food'   

class AboutUs(TemplateView):
    template_name = 'about_us.html'

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

  
class ContactUsView(FormView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm
    success_url = '/contact-us-sent/'       

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 

class Contact_us_sent(TemplateView):
    template_name = 'contact_us_sent.html'      

   



