from django.contrib import messages
from django.views.generic import ListView,DetailView,TemplateView,FormView
from .models import Food,Order
from .forms import ContactUsForm,OrderForm
from django.urls import reverse_lazy



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
    success_url = reverse_lazy('contact-us-sent')       

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 

class Contact_us_sent(TemplateView):
    template_name = 'contact_us_sent.html'      


class OrderView(FormView):
    template_name = 'order.html'
    form_class = OrderForm
    success_url = reverse_lazy('order-success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        food_id = self.kwargs.get('pk')
        if food_id:
            try:
                context['food'] = Food.objects.get(pk=food_id)
            except Food.DoesNotExist:
                context['food'] = None
        return context

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['name'] = self.request.user.get_full_name() or self.request.user.username
            initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        order = form.save(commit=False)
        if self.request.user.is_authenticated:
            order.user = self.request.user
        order.save()
        
        messages.success(self.request, f'✅ سفارش شما با موفقیت ثبت شد! شماره سفارش: {order.id}')
        return super().form_valid(form)

class OrderSuccessView(TemplateView):
    template_name = 'order_successful.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.last()
        return context



