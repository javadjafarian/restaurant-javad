from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from restaurantblog.models import Order
from django.contrib.auth import logout
from django.views import View


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        messages.success(self.request, '✅ ثبت‌نام شما با موفقیت انجام شد! حالا وارد شوید.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '❌ لطفاً خطاها را اصلاح کنید.')
        return super().form_invalid(form)



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, f'✅ خوش آمدید {self.request.user.username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '❌ نام کاربری یا رمز عبور اشتباه است.')
        return super().form_invalid(form)



class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, '✅ شما با موفقیت خارج شدید.')
        return redirect('home')



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user).order_by('-id')
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'accounts/profile-edit.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, '✅ اطلاعات شما با موفقیت به‌روزرسانی شد!')
        return super().form_valid(form)