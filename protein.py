import requests

def get_protein_amount(food_name, api_key):
    global protein_amount
    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {
        "api_key": api_key,
        "query": food_name
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()
        if data.get("foods"):
            food = data["foods"][0]
            nutrients = food.get("foodNutrients")
            protein_info = next((nutrient for nutrient in nutrients if nutrient["nutrientName"] == "Protein"), None)
            if protein_info:
                protein_amount = protein_info["value"]
                return protein_amount
        else:
            print("Alimento no encontrado en la base de datos.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

api_key = "geUu0kVWsLwNEH7eg9fiDZyz4KdAgLsqAdrOdcdg"