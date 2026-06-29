from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.urls import reverse

User = get_user_model()


class FoodType(models.Model):
    title = models.CharField(max_length=255) 

    def __str__(self):
        return f'{self.title}'


class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=255, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True) 
    description = models.TextField()
    price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='food_images/')
    food_types = models.ManyToManyField(to=FoodType)

    def __str__(self):
        return f"{self.name} - {self.price} Tooman"
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    
class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=True) 
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=11, blank=True)
    text = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.email}"


class Order(models.Model):
    # ✅ اضافه کردن ارتباط با کاربر
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='orders'
    )
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11, 'wrong number')])
    email = models.EmailField(max_length=254, blank=True)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ تاریخ ثبت سفارش
    
    def __str__(self):
        return f"سفارش #{self.id} - {self.name}"
    
    def get_total_price(self):
        # اینجا می‌تونی قیمت کل رو محاسبه کنی
        return self.amount * 10000  # مثال