import requests

def forcast(city_name, api_key):
    # URL for the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"

    try:
        # Send a GET request to the API URL
        response = requests.get(url)
        # Parse the JSON response
        data = response.json()
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Extract weather information from the response data
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Display weather information to the user
            print(f"Weather in {city_name}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature}°F")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} f/s")
        else:
            # Print an error message if the response status code is not 200
            print("Error: Please check your input and try again.")
    
    except Exception as e:
        # Handle any exceptions that occur during the API request
        print(f"An error occurred: {e}")

# API key from OpenWeatherMap (Replace this with your actual API key)
api_key = '6927a1742ef9e64755583799244f1387'
# Prompt the user to enter a city name
city_name = input("Enter city name: ")
# Call the forecast function with the provided city name and API key
forcast(city_name, api_key)