from django.db import models


class FoodType(models.Model):
    title = models.CharField(max_length=255) 


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
    
class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=True) 
    email = models.EmailField(max_length=254)
    phone_number =  models.CharField(max_length=11, blank=True)
    text = models.TextField()  