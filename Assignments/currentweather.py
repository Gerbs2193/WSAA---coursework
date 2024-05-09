import requests

# Used functions as I used two separate apis and functionalities aka temp and wind direction. 
def get_current_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
    # Get request sent to the api needed 
    response = requests.get(url)
    data = response.json()
    temperature = data['current']['temperature_2m']
    return temperature

def get_current_wind_direction(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=wind_direction_10m"
    response = requests.get(url)
    data = response.json()
    current_wind_direction = data['current']['wind_direction_10m']
    return current_wind_direction

# Lat and Long of my current address
def main():
    latitude = 53.349805
    longitude = -6.26031

    temperature = get_current_weather()
    print(f"Current Temperature: {temperature}°C")

    wind_direction = get_current_wind_direction(latitude, longitude)
    print(f"Current Wind Direction: {wind_direction}°")
# importability
if __name__ == "__main__":
    main()
