import requests
import os
from dotenv import load_dotenv

load_dotenv()

def gardening(item: str):
    api_key = os.getenv("gardening_api")
    if not api_key:
        return {"error": "API key not found. Please set gardening_api in .env"}

    url = f"https://perenual.com/api/v2/species-list?key={api_key}&q={item}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch plant data: {e}"}

    data = response.json()
    plants_data = data.get("data")

    if not plants_data:
        return {"error": f"No plant found for '{item}'."}
    plant = plants_data[0]

    common = plant.get("common_name", "N/A")
    scientific = plant.get("scientific_name", "N/A")
    family = plant.get("family", "N/A")

    return f"The {item} is commonly known as {common}, with the scientific name {scientific}, and belongs to the family {family}."
