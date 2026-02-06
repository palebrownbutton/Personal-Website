import requests

def cooking(item: str):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={item}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Failed to fetch recipes for '{item}'."

    data = response.json()
    meals = data.get('meals')

    if not meals:
        return f"No recipe found for '{item}'."

    meal = meals[0] 
    name = meal.get('strMeal', 'N/A')
    category = meal.get('strCategory', 'N/A')
    area = meal.get('strArea', 'N/A')
    instructions = meal.get('strInstructions', 'N/A')

    ingredients = []
    for i in range(1, 21):
        ingredient = meal.get(f'strIngredient{i}')
        measure = meal.get(f'strMeasure{i}')
        if ingredient and ingredient.strip():
            if measure and measure.strip():
                ingredients.append(f"{measure.strip()} {ingredient.strip()}")
            else:
                ingredients.append(ingredient.strip())

    recipe_text = f"Recipe for {name}:\n"
    recipe_text += f"Category: {category}\n"
    recipe_text += f"Area: {area}\n"
    recipe_text += f"Instructions: {instructions}\n"
    recipe_text += "Ingredients:\n"
    for ing in ingredients:
        recipe_text += f"- {ing}\n"

    return recipe_text
