from django.contrib import admin
from .models import Food,Consume

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'carbohydrates', 'protein', 'fats', 'calories')


@admin.register(Consume)
class ConsumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_consume')
