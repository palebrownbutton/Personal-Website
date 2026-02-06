import requests

def cooking(item: str):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={item}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch recipes."}

    data = response.json()
    meals = data.get('meals')

    if not meals:
        return {"error": f"No recipe found for '{item}'."}

    recipes = []
    for meal in meals:
        ingredients = []
        for i in range(1, 21):
            ingredient = meal.get(f'strIngredient{i}')
            measure = meal.get(f'strMeasure{i}')
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure.strip()} {ingredient.strip()}" if measure else ingredient.strip())
        recipe_info = {
            "name": meal.get('strMeal'),
            "category": meal.get('strCategory'),
            "area": meal.get('strArea'),
            "instructions": meal.get('strInstructions'),
            "ingredients": ingredients,
        }
        recipes.append(recipe_info)

    return {"recipes": recipes}
