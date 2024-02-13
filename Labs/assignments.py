# Needed for msking http request to api
import requests

# current weather data from api
def get_current_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"

    # Get request with the response from server
    response = requests.get(url)
    data = response.json()
    temperature = data['current']['temperature_2m']
    wind_speed = data['current']['wind_speed_10m']
    return temperature, wind_speed

if __name__ == "__main__":
    temperature, wind_speed = get_current_weather()
    print(f"Current Temperature: {temperature}°C")
    print(f"Current Wind Speed: {wind_speed} km/h")