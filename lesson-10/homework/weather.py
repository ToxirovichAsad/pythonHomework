import requests
import os

def get_weather(city: str):
    """Fetch weather data for a given city."""
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "b8ec92fded373e0cde6d50e9e8361dad")
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)
        response.raise_for_status() 

        data = response.json()
        if "main" not in data:
            print("City not found. Please enter a valid city name.")
            return None

        return {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Condition": data["weather"][0]["description"].capitalize(),
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Data not found ")
        return None

def main():
    """Main function for user interaction."""
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        
        weather = get_weather(city)
        if weather:
            for key, value in weather.items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()
