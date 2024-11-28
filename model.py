import requests
import pandas as pd

# Set the base URL for Google Places Text Search API
BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

def get_businesses_text_search(api_key, query=""):
    params = {
        "query": query,
        "key": api_key
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        businesses = []

        for result in results:
            business = {
                "name": result.get("name"),
                "address": result.get("formatted_address"),
                "place_id": result.get("place_id"),
                "latitude": result["geometry"]["location"]["lat"],
                "longitude": result["geometry"]["location"]["lng"],
                "rating": result.get("rating"),
                "user_ratings_total": result.get("user_ratings_total")
            }
            businesses.append(business)
        
        return businesses
    else:
        print("Error:", response.status_code, response.text)
        return []

def save_to_csv(businesses, filename="businesses.csv"):
    """
    Saves the list of businesses to a CSV file.
    
    Args:
    - businesses (list): List of business dictionaries with details like name, address, etc.
    - filename (str): Name of the CSV file to save the data.
    """
    # Convert to DataFrame
    df = pd.DataFrame(businesses)
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Define your API key
API_KEY = "YOUR_API_KEY_HERE"

# Get nearby businesses
businesses = get_businesses_text_search(API_KEY)

# Save the data to a CSV file
save_to_csv(businesses, filename="marketing_agencies_near_strandzha35.csv")
