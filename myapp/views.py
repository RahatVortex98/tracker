from django.shortcuts import redirect, render  # Import the render function to render templates.
from .models import Food, Consume  # Import the Food and Consume models from the current app.

# Create your views here. (A placeholder comment typically left by Django when the app is created.)

def index(request):
    total_calories = 0
    calorie_goal = 2000 
    
    # Check if the request is a POST request, which indicates form submission.
    if request.method == "POST":
        # Get the selected food item from the form data submitted via POST.
        food_consume = request.POST["food_consume"]
        
        # Retrieve the Food object that matches the selected food name.
        # Note: This assumes food names are unique. If they are not, this could raise errors.
        consume = Food.objects.get(name=food_consume)
        
        # Get the currently logged-in user (Django provides this through request.user).
        user = request.user
        
        # Create a new Consume object, linking the user with the selected food.
        consume = Consume(user=user, food_consume=consume)
        
        # Save the new Consume object to the database.
        consume.save()
        
        # Fetch all food items to display in the template after the form is submitted.
        foods = Food.objects.all()
        # Calculate total consumed calories
        consumed_items = Consume.objects.filter(user=request.user)
        total_calories = sum(item.food_consume.calories for item in consumed_items)
        calorie_goal = 2000  # Example goal

    else:
        # If the request is not a POST request (e.g., GET request),
        # fetch all food items for the initial page load.
        foods = Food.objects.all()
    consumed_food=Consume.objects.filter(user=request.user)
    total_calories = 0
    calorie_goal = 2000 
  
    # Render the 'home.html' template, passing the foods QuerySet to the context.
    return render(request, 'home.html', {'foods': foods,'consumed_food':consumed_food,'total_calories': total_calories,
    'calorie_goal': calorie_goal,})



def delete(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'delete.html')


