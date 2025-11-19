from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample data
RECIPES = [
    {
        'id': 1, 'name': 'Chicken Stir Fry', 'category': 'Dinner', 
        'ingredients': ['chicken', 'rice', 'vegetables', 'soy sauce'],
        'nutrition': {'calories': 450, 'protein': 35, 'carbs': 40, 'fat': 15},
        'cost': 8.50, 'cook_time': 25, 'difficulty': 'Easy'
    },
    {
        'id': 2, 'name': 'Oatmeal Breakfast', 'category': 'Breakfast',
        'ingredients': ['oats', 'milk', 'banana', 'honey'],
        'nutrition': {'calories': 350, 'protein': 12, 'carbs': 60, 'fat': 8},
        'cost': 2.50, 'cook_time': 10, 'difficulty': 'Easy'
    },
    {
        'id': 3, 'name': 'Salmon Salad', 'category': 'Lunch',
        'ingredients': ['salmon', 'lettuce', 'tomato', 'cucumber', 'dressing'],
        'nutrition': {'calories': 380, 'protein': 30, 'carbs': 15, 'fat': 25},
        'cost': 12.00, 'cook_time': 15, 'difficulty': 'Easy'
    },
    {
        'id': 4, 'name': 'Pasta Carbonara', 'category': 'Dinner',
        'ingredients': ['pasta', 'eggs', 'bacon', 'cheese', 'cream'],
        'nutrition': {'calories': 520, 'protein': 25, 'carbs': 55, 'fat': 22},
        'cost': 6.75, 'cook_time': 20, 'difficulty': 'Medium'
    },
    {
        'id': 5, 'name': 'Smoothie Bowl', 'category': 'Breakfast',
        'ingredients': ['yogurt', 'berries', 'granola', 'honey'],
        'nutrition': {'calories': 280, 'protein': 15, 'carbs': 45, 'fat': 6},
        'cost': 4.25, 'cook_time': 5, 'difficulty': 'Easy'
    }
]

class MealPlanner:
    def __init__(self):
        self.inventory = []
        self.user_goals = {}
        
    def set_user_goals(self, goals):
        self.user_goals = goals
        
    def add_to_inventory(self, item):
        self.inventory.append(item)
        
    def generate_meal_plan(self, days=7, budget=100):
        meal_plan = []
        total_cost = 0
        
        for day in range(days):
            date = datetime.now() + timedelta(days=day)
            day_plan = {
                'date': date.strftime('%Y-%m-%d'),
                'day_name': date.strftime('%A'),
                'meals': []
            }
            
            # Select meals for the day
            for meal_type in ['Breakfast', 'Lunch', 'Dinner']:
                suitable_recipes = self.get_suitable_recipes(meal_type)
                if suitable_recipes:
                    selected_meal = random.choice(suitable_recipes)
                    day_plan['meals'].append(selected_meal)
                    total_cost += selected_meal['cost']
            
            meal_plan.append(day_plan)
        
        return {
            'meal_plan': meal_plan,
            'total_cost': round(total_cost, 2),
            'budget_status': 'Under Budget' if total_cost <= budget else 'Over Budget'
        }
    
    def get_suitable_recipes(self, meal_type):
        suitable = [r for r in RECIPES if r['category'] == meal_type]
        
        # Filter based on user goals
        if self.user_goals.get('diet_type'):
            if self.user_goals['diet_type'] == 'vegetarian':
                suitable = [r for r in suitable if 'chicken' not in r['ingredients'] and 'bacon' not in r['ingredients'] and 'salmon' not in r['ingredients']]
            elif self.user_goals['diet_type'] == 'low_carb':
                suitable = [r for r in suitable if r['nutrition']['carbs'] < 30]
        
        # Filter based on inventory
        if self.inventory:
            suitable = [r for r in suitable if any(ingredient in self.inventory for ingredient in r['ingredients'])]
            
        return suitable
    
    def generate_shopping_list(self, meal_plan):
        all_ingredients = []
        for day in meal_plan:
            for meal in day['meals']:
                all_ingredients.extend(meal['ingredients'])
        
        # Remove duplicates and inventory items
        shopping_list = list(set(all_ingredients) - set(self.inventory))
        return sorted(shopping_list)

planner = MealPlanner()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', recipes=RECIPES)

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    data = request.json
    
    # Set user goals
    planner.set_user_goals({
        'diet_type': data.get('diet_type', 'balanced'),
        'calorie_goal': data.get('calorie_goal', 2000),
        'budget': data.get('budget', 100)
    })
    
    # Set inventory
    planner.inventory = data.get('inventory', [])
    
    # Generate meal plan
    meal_plan = planner.generate_meal_plan(
        days=data.get('days', 7),
        budget=data.get('budget', 100)
    )
    
    # Generate shopping list
    shopping_list = planner.generate_shopping_list(meal_plan['meal_plan'])
    
    return jsonify({
        'meal_plan': meal_plan,
        'shopping_list': shopping_list
    })

@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    data = request.json
    item = data.get('item', '').strip().lower()
    
    if item and item not in planner.inventory:
        planner.inventory.append(item)
    
    return jsonify({'inventory': planner.inventory})

if __name__ == '__main__':
    print("Meal Planner AI started at http://localhost:5000")
    app.run(debug=True, port=5000)
