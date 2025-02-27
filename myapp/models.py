from django.db import models
from django.contrib.auth.models import User


# Carbohydrates: 1 gram = 4 calories
# Proteins: 1 gram = 4 calories
# Fats: 1 gram = 9 calories
class Food(models.Model):
    name = models.CharField(max_length=100)
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField(editable=False)  # Ensure this is not user-editable
    
    def save(self, *args, **kwargs):
       
        self.calories = int(self.carbohydrates * 4 + self.protein * 4 + self.fats * 9)
        super(Food, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Consume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food_consume = models.ForeignKey(Food,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.user
    
