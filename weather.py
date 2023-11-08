import requests
import json
import time

API_BASE_URL = "https://api.weatherapi.com/v1/"
API_KEY = "66cd67e9fed64140885124214230511"  

favorite_cities = []

def get_weather_by_city(city):
    url = f"{API_BASE_URL}current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        print(f"Error: {data['error']['message']}")
    else:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")

def add_favorite_city(city):
    favorite_cities.append(city)
    print(f"{city} added to your favorite cities.")

def view_favorite_cities():
    if favorite_cities:
        print("Your favorite cities:")
        for city in favorite_cities:
            print(city)
    else:
        print("You don't have any favorite cities yet.")

def update_favorite_city(old_city, new_city):
    if old_city in favorite_cities:
        favorite_cities.remove(old_city)
        favorite_cities.append(new_city)
        print(f"{old_city} updated to {new_city}.")
    else:
        print(f"{old_city} is not in your favorite cities.")

def delete_favorite_city(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"{city} removed from your favorite cities.")
    else:
        print(f"{city} is not in your favorite cities.")

def auto_refresh():
    while True:
        if favorite_cities:
            for city in favorite_cities:
                get_weather_by_city(city)
        else:
            print("No favorite cities to auto-refresh.")
        time.sleep(30)  

def main_menu():
    while True:
        print("Weather Checking Application")
        print("1. Check weather by city")
        print("2. Manage favorite cities")
        print("3. Auto-refresh")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter the city name: ")
            get_weather_by_city(city)
        elif choice == "2":
            print("Favorite City Operations:")
            print("1. Add a city to favorites")
            print("2. View favorite cities")
            print("3. Update a favorite city")
            print("4. Delete a favorite city")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                city = input("Enter the city to add to favorites: ")
                add_favorite_city(city)
            elif sub_choice == "2":
                view_favorite_cities()
            elif sub_choice == "3":
                old_city = input("Enter the old city name: ")
                new_city = input("Enter the new city name: ")
                update_favorite_city(old_city, new_city)
            elif sub_choice == "4":
                city = input("Enter the city to delete from favorites: ")
                delete_favorite_city(city)
            else:
                print("Invalid choice. Please try again.")
        elif choice == "3":
            auto_refresh()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
