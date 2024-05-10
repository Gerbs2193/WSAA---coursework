# WSAA---coursework - Gerard Ball

## Table of Contents
- [What-is-it](#what-is-it)
- [Task1-currentweather.py](#task1-currentweatherpy)
- [Task2-assignment03-cso.py](#task2-assignment03-csopy)
- [Task3-assignment04-github.py](#task3-assignment04-githubpy)
- [Resources and Commentary](#resources-and-commentary)
- [Bibliography](#bibliography)

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
Ensure you have python and the requests library installed on your computer. Both will be needed for this task.

**Step 2**
Going by my own attempt; define two functions that each independently fetch weather data from two separate API's. The main function was used to ensure this script runs properly

**Step 3** Simply print out the current temperature and current wind direction. 

**How to run**
 1. Open Github and visit my repository at https://github.com/Gerbs2193/WSAA---coursework.

 2. Download the script: Click the code button and then download the Zip.

 3. Extraction: Add to your own directory 

 4. Open a terminal or in my case, vscode

 5. navigate to the script's directory, then simply run it using python currentweather.py. 

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
You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.

**What is being asked here?**

Write a program that will retreive the dataset for the exchequer account historical series from the CSO and simply store it in a local file called cso.json

**Step 1**

Like before, ensure all dependancies are installed like python and the requests library as well as Pandas and JSON. All will be needed for this here.

**Step 2**
import pandas and JSON libraries. Define the CSO URL (which after an exhaustive effort, was actually found by just typing into google: 'exchequer account historical series cso JSON)' rather than going to the CSO and manually attempting to find it, as I did initially. Use Pandas to then read the data from them URL and then convert it to JSON. Lastly in keeping to the brief, write the JSON to a file called cso.json. 

**How to run**

As before, open Github and visit my repository at https://github.com/Gerbs2193/WSAA---coursework and Simply folllow the same steps as with the first task until you have gotten to running the script. Then, simply type in python assignment03-cso.py in the terminal and away you go. 

**Final Code**

```
import pandas as pd

import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

df = pd.read_json(url)

data = df.to_json()

with open("cso.json", "w") as f:
    f.write(data)
```````









## Task3-assignment04-github.py
**The brief:**

>Write a program in python that will read a file from a repository, 
The program should then replace all the instances of the text "Andrew" with your name. 
The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
I do not need to see your keys (see lab2, to follow 

**What to do?**

From my understanding, write a txt file in, say, VScode. In it, write the word Andrew a number of times. Push it to the repository that is being used for the above tasks aka WSAA---coursework. Then you write the program that will read in this txt file to ultimately change the word Andrew with your name, also known in many circles as Ger, for me. 

**Step 1**

Ensure all dependancies are installed like git module to which we import the class repo as needed to interact with our git repository. Import OS and Shutil for navigating directories and utility. 

**Step 2**
Code it. Start with the pertinent information of the repository like its URL, the file path of the txt file and your name to replace the Andrew instances. Clone the repo. Read and modify the txt file as per the brief. Write the new file and commit it to Github. 

**Step3**

Authentication is required given that the brief tasks us with pushing commits. To do this, I created an SSH key and agent and opened it up in Github. To do this, type ssh-keygen -t rsa -b 4096 -C your_email@example.com in the terminal. On mac, type eval "$(ssh-agent -s) to set up the agent or ssh-add ~/.ssh/id_rsa on Windows. Add it on Github by navigating the settings and pasting the SSH key into the necessary field section. This caused me some grief as i kept getting erorrs relating to my ssh. Got it in the end. 



**How to run**
Same steps as before but the script it called assignment04-github.py. Given it's authentication requirement, input ***** when asked to do so and the program will carry out. 


**Conpleted code**

```
from git import Repo 
import os
import shutil

REPO_URL = 'git@github.com:Gerbs2193/WSAA---coursework.git'
FILE_PATH = 'Assignments/Andrew.txt'
YOUR_NAME = 'Ger'

if os.path.exists('/tmp/repo'):
    shutil.rmtree('/tmp/repo')

repo = Repo.clone_from(REPO_URL, '/tmp/repo')

with open(os.path.join('/tmp/repo', FILE_PATH), 'r') as file:
    filedata = file.read()

filedata = filedata.replace('Andrew', YOUR_NAME)

with open(os.path.join('/tmp/repo', FILE_PATH), 'w') as file:
    file.write(filedata)

try:
    repo.git.add(FILE_PATH)
    repo.git.commit('-m', 'Replace Andrew with ger')
    repo.git.push()
    print("Changes pushed successfully!")
except Exception as e:
    print(f'An error has occurred: {e}')

repo.close()
shutil.rmtree('/tmp/repo')
```

## Resources and Commentary

**currentweather.py**

- https://open-meteo.com/ - Used to refresh on how to make requests and the like. 

- https://docs.python.org/3/library/json.html - Huge resourse that had most all that I needed. 

- https://stackoverflow.com/questions/70408634/openweather-api-get-current-temp-with-discord-py - Used to see requests of api in action

**Issues**

I didnt know how to get the wind direction as that data wasn't available from the first api provided. I somehow missed the second one. 

**assignment03-cso.py**

- https://stackoverflow.com/questions/34493531/how-to-store-and-retrieve-json-data-into-local-storage - Answered the brief and showed how to do it. 

**assignment04-github.py**

- https://stackoverflow.com/questions/71750303/how-to-link-ssh-key-to-ssh-agent-and-push-files-to-github-account - Helped with authentication help and file path coding

- https://github.com/github/docs/blob/main/content/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.md - Thorough walkthrough of steps

- https://stackoverflow.com/questions/63001496/how-to-export-multiple-temp-sql-tables-into-multiple-excel-tabs - code example similiar to my own. 

- https://stackoverflow.com/questions/67706647/how-to-add-commit-and-push-a-repository-via-git-python - Helped with cloning

- https://gitpython.readthedocs.io/en/stable/ - Used to know how to interact with the repo, cloning and commiting the changes. 

**Issues** 

Creating the SSH pair wouldn't work and for the longest time in the terminal app on my mac and i still am unsure why. Eventually, I did it via the vscode terminal and it worked somehow. 

## Bibliography

 - Open. Available at: https://open-meteo.com/ (Accessed: 10 May 2024). 

 - JSON - JSON encoder and decoder (no date) Python documentation. Available at: https://docs.python.org/3/library/json.html (Accessed: 10 May 2024). 

 - Stackoverflow OpenWeather API get current temp. with discord.py, Stack Overflow. Available at: https://stackoverflow.com/questions/70408634/openweather-api-get-current-temp-with-discord-py (Accessed: 10 May 2024). 

 - Stackoverflow. How to store and retrieve JSON data into local storage?, Stack Overflow. Available at: https://stackoverflow.com/questions/34493531/how-to-store-and-retrieve-json-data-into-local-storage (Accessed: 10 May 2024). 

 - Stackoverflow. How to link SSH key to SSH agent and push files to github account, Stack Overflow. Available at: https://stackoverflow.com/questions/71750303/how-to-link-ssh-key-to-ssh-agent-and-push-files-to-github-account (Accessed: 10 May 2024). 

 - Github, Docs/content/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.MD at main · github/docs, GitHub. Available at: https://github.com/github/docs/blob/main/content/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.md (Accessed: 10 May 2024). 

 - Stackoverflow.  Export SQL query to excel with multiple worksheets and custom headers, Stack Overflow. Available at: https://stackoverflow.com/questions/28685906/export-sql-query-to-excel-with-multiple-worksheets-and-custom-headers (Accessed: 10 May 2024). 

 - Stackoverflow. How to add/commit and push a repository via Git-Python?, Stack Overflow. Available at: https://stackoverflow.com/questions/67706647/how-to-add-commit-and-push-a-repository-via-git-python (Accessed: 10 May 2024). 

 - GitPython documentation (no date) GitPython Documentation - GitPython 3.1.43 documentation. Available at: https://gitpython.readthedocs.io/en/stable/ (Accessed: 10 May 2024). 