# WSAA---coursework

## What is it

This README concentrates on the steps needed to run, research and ultimately understand the three assignments set by professor Andrew Beatty as part of ATU's Web Services and Applications module. 

As stated; there are three assignments:

- currentweather.py
- assignment03-cso.py
- assignment04-github.py

## Task1-currentweather.py

**The brief was as follows;**
>Using the URL below
https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
Write a python program called currentweather.py that will print out the current temperature on the console (and only the temperature)
I have set the lat/long to my location, you may use that or a different location.
Last few marks:
Look at the documentation (below) and print out the current wind direction (10m) as well.
🌤️ Free Open-Source Weather API | Open-Meteo.com

**What is being asked here?**

Using both urls, you are to create a program that will print the current weather from one and the current wind direction from the other. 

**Step 1**
Ensure you have all python and the requests library installed on your computer. Both will be needed for this task.

**Step 2**
Going by my own attempt; define two functions that each independently fetch weather data from two separate API's. The main function was used to ensure this script runs properly

**Step 3** Simply print out the current temperature and current wind direction. 

**How to run**
 1. Open Github and visit my repository at https://github.com/Gerbs2193/WSAA---coursework.

 2. Download the script: Click the code button and then download the Zip.

 3. Extraction: Add to your own directory 

 4. Open a terminal or in my case, vscode

 5. navigate to the script's directory, then simply run it using python current_weather.py. 

 **Final Code**

 ```
 python
import requests

def get_current_weather():
url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
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

def main():
latitude = 53.349805
longitude = -6.26031

temperature = get_current_weather()
print(f"Current Temperature: {temperature}°C")

wind_direction = get_current_wind_direction(latitude, longitude)
print(f"Current Wind Direction: {wind_direction}°")

if name == "main":
main()
```

## Task2-assignment03-cso.py

**The brief was as follows**:

>Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
Upload this program to the same repository you used for the XML assignment
Save this assignment as "assignment03-cso.py"
This program should not be a long one
I don't need you to reformat or analyse the data in any way
It should be about 10ish lines long (I have not counted)
You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.>

**What is being asked here?**

Write a program that will retreive the dataset for the exchequer account historical series from the CSO and simply store it in a local file called cso.json

**Step 1**

Like before, ensure all dependancies are installed like python and the requests library as well as Pandas and JSON. All will be needed for this here.

**Step 2**
import pandas and JSON libraries. Define the CSO URL (which after an exhaustive effort, was actually found by just typing into google: 'exchequer account historical series cso JSON)' rather than going to the CSO and manually attempting to find it, as I did initially. Use Pandas to then read the data from them URL and then convert it to JSON. Lastly in keeping to the brief, write the JSON to a file called cso.json. 
