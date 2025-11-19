# Meal Planner AI - Smart Meal Planning Application

## Overview

Meal Planner AI adalah aplikasi web yang membantu pengguna merencanakan menu makanan berdasarkan tujuan diet, budget, dan bahan makanan yang tersedia. Aplikasi ini menggunakan algoritma cerdas untuk menghasilkan rencana makan yang personalized.

## Struktur Folder

```
meal_planner/
├── app.py                 # Aplikasi Flask utama
├── requirements.txt       # Dependencies Python
├── templates/
│   ├── index.html        # Halaman utama - Meal Planner
│   └── dashboard.html    # Halaman dashboard - Recipe Collection
```

## Dataset & Resep yang Tersedia

### Resep Makanan (5 Resep Sample)

1. **Chicken Stir Fry** (Dinner)
   - **Ingredients**: chicken, rice, vegetables, soy sauce
   - **Nutrition**: 450 cal, 35g protein, 40g carbs, 15g fat
   - **Cost**: $8.50 | **Time**: 25min | **Difficulty**: Easy

2. **Oatmeal Breakfast** (Breakfast) 
   - **Ingredients**: oats, milk, banana, honey
   - **Nutrition**: 350 cal, 12g protein, 60g carbs, 8g fat
   - **Cost**: $2.50 | **Time**: 10min | **Difficulty**: Easy

3. **Salmon Salad** (Lunch)
   - **Ingredients**: salmon, lettuce, tomato, cucumber, dressing
   - **Nutrition**: 380 cal, 30g protein, 15g carbs, 25g fat
   - **Cost**: $12.00 | **Time**: 15min | **Difficulty**: Easy

4. **Pasta Carbonara** (Dinner)
   - **Ingredients**: pasta, eggs, bacon, cheese, cream
   - **Nutrition**: 520 cal, 25g protein, 55g carbs, 22g fat
   - **Cost**: $6.75 | **Time**: 20min | **Difficulty**: Medium

5. **Smoothie Bowl** (Breakfast)
   - **Ingredients**: yogurt, berries, granola, honey
   - **Nutrition**: 280 cal, 15g protein, 45g carbs, 6g fat
   - **Cost**: $4.25 | **Time**: 5min | **Difficulty**: Easy

## Fitur Utama

### 1. Personalization Goals
- **Diet Type**: Balanced, Vegetarian, Low Carb
- **Weekly Budget**: Customizable ($50-500)
- **Planning Period**: 1-14 hari
- **Calorie Goals**: Target kalori harian

### 2. Inventory Management
- **Add Ingredients**: Input bahan yang sudah tersedia
- **Real-time Updates**: Inventory list yang dinamis
- **Smart Filtering**: Resep berdasarkan bahan yang ada

### 3. AI Meal Planning
- **Automatic Meal Selection**: Berdasarkan diet type dan inventory
- **Budget Optimization**: Menyesuaikan dengan budget mingguan
- **Nutrition Balance**: Kombinasi makanan yang seimbang
- **Variety Assurance**: Tidak ada repetisi berlebihan

### 4. Shopping List Generation
- **Auto-generated List**: Bahan yang perlu dibeli
- **Inventory Deduction**: Hanya bahan yang tidak ada
- **Organized Output**: List yang terstruktur

## Teknologi yang Digunakan

### Backend
- **Flask 2.3.3** - Web framework Python
- **Pandas 2.1.4** - Data manipulation

### Frontend
- **HTML5/CSS3** - Responsive design
- **Vanilla JavaScript** - Client-side functionality
- **Modern CSS** - Flexbox dan Grid layout

### AI & Logic
- **Rule-based Algorithm** - Filtering dan selection
- **Randomized Selection** - Dengan constraints
- **Cost Optimization** - Budget management

## Cara Menjalankan

### 1. Install Dependencies
```bash
cd meal_planner
pip install -r requirements.txt
```

### 2. Run Application
```bash
python app.py
```

### 3. Access Application
Buka browser: `http://localhost:5000`

## Cara Penggunaan

### Step 1: Set Goals
1. Pilih **Diet Type** (Balanced/Vegetarian/Low Carb)
2. Tentukan **Weekly Budget** 
3. Pilih **Days to Plan** (1-14 hari)

### Step 2: Manage Inventory
1. Input bahan makanan yang sudah ada
2. Klik "Add to Inventory"
3. Lihat inventory yang terkumpul

### Step 3: Generate Plan
1. Klik "Generate Meal Plan"
2. Tunggu proses AI planning
3. Lihat hasil meal plan dan shopping list

## API Endpoints

### POST `/generate_plan`
Generate meal plan berdasarkan user input:
```json
{
  "diet_type": "vegetarian",
  "budget": 100,
  "days": 7,
  "inventory": ["rice", "eggs"]
}
```

### POST `/add_inventory`
Tambah item ke inventory:
```json
{
  "item": "chicken"
}
```

## Algoritma Planning

### 1. Recipe Filtering
```python
# Filter by meal type
suitable = [r for r in RECIPES if r['category'] == meal_type]

# Filter by diet type
if diet_type == 'vegetarian':
    suitable = [r for r in suitable if no_meat_ingredients(r)]

# Filter by inventory
suitable = [r for r in suitable if has_inventory_ingredients(r)]
```

### 2. Meal Selection
- Random selection dari filtered recipes
- Budget constraint checking
- Nutrition balance consideration

### 3. Shopping List Generation
```python
all_ingredients = extract_from_meal_plan(meal_plan)
shopping_list = all_ingredients - user_inventory
```

## Customization Options

### Menambah Resep Baru
Edit list `RECIPES` di `app.py`:
```python
{
    'id': 6,
    'name': 'New Recipe',
    'category': 'Lunch',
    'ingredients': ['ingredient1', 'ingredient2'],
    'nutrition': {'calories': 400, 'protein': 20, 'carbs': 50, 'fat': 15},
    'cost': 10.00,
    'cook_time': 30,
    'difficulty': 'Easy'
}
```

### Modifikasi Diet Rules
Edit di method `get_suitable_recipes`:
```python
# Add new diet type
elif self.user_goals['diet_type'] == 'keto':
    suitable = [r for r in suitable if r['nutrition']['carbs'] < 20]
```

### Adjust Budget Calculations
Modifikasi di `generate_meal_plan`:
```python
# Change cost calculation logic
total_cost += selected_meal['cost'] * adjustment_factor
```

## Use Cases

### Untuk Keluarga
- **Meal planning** mingguan
- **Budget management** belanja
- **Nutrition tracking** untuk anggota keluarga
- **Time saving** dalam decision making

### Untuk Health Enthusiasts
- **Diet compliance** dengan goals spesifik
- **Macro tracking** protein/carbs/fat
- **Recipe variety** untuk menghindari kebosanan
- **Cost efficiency** healthy eating

### Untuk Single Person
- **Minimizing waste** dengan inventory-based planning
- **Simple cooking** dengan difficulty level
- **Quick meals** dengan cook time consideration
- **Budget control** untuk eating habit

## Keunggulan

### 1. Personalization
- Setiap user dapat custom goals
- Inventory-based recommendations
- Budget-aware meal selection

### 2. Practicality
- Menggunakan bahan yang sudah ada
- Realistic cooking times
- Achievable difficulty levels

### 3. User Experience
- Interface yang sederhana
- Process yang straightforward
- Hasil yang actionable

## Development Notes

### Data Structure
- **Recipes**: Dictionary dengan nutrition info
- **Meal Plan**: Array of days dengan meals
- **Inventory**: Simple list of ingredients
- **User Goals**: Dictionary dengan preferences

### Scalability Considerations
- Database integration untuk large recipe collections
- User authentication untuk personalized history
- Advanced ML algorithms untuk better recommendations
- Mobile app development

## Support & Troubleshooting

### Common Issues
1. **Port already in use** - Ganti port di `app.run(port=5001)`
2. **Import errors** - Pastikan Flask dan Pandas terinstall
3. **No recipes showing** - Check recipe data structure

### Debug Mode
Aktifkan debug mode untuk development:
```python
app.run(debug=True, port=5000)
```

---

**Meal Planner AI** - Solusi praktis untuk meal planning yang personalized, budget-aware, dan inventory-smart. Membantu membuat keputusan makan yang lebih sehat dan efisien.
