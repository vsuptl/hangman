import datetime as dt
from tkinter import font
import requests
import tkinter as tk
from tkinter import PhotoImage

img = None


def getWeather():
    global img
    city = userinput.get()
    API_KEY = "e627f9024fbba9d0b4699af4914fc1b3"

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}")
    print(weather_data.json())
    if weather_data.status_code == 200:
        descriptionWeather = weather_data.json()['weather'][0]['main']
        temperature = weather_data.json()['main']['temp']
        print("The weather in " + city + " is" + " " + str(temperature) + " degrees")
        print(descriptionWeather)

        if descriptionWeather == "Clouds":
            img = PhotoImage(file="resources/cloudy.png")
            img = img.subsample(2, 2)
        elif descriptionWeather == "Clear":
            img = PhotoImage(file="resources/sunny.png")
            img = img.subsample(2, 2)
        elif descriptionWeather == "Snow":
            img = PhotoImage(file="resources/snowy")
            img = img.subsample(2, 2)
        elif descriptionWeather == "Rain":
            img = PhotoImage(file="resources/rainy")
            img = img.subsample(2, 2)

        weatherPicture = tk.Label(image=img)
        weatherPicture.grid(row=3, column=0, pady=10)

        temperatureText = tk.Label(text=temperature, font=font.Font(size=20))
        temperatureText.grid(row=4, column=0, pady=10)

        description = tk.Label(text=descriptionWeather, font=font.Font(size=20))
        description.grid(row=5, column=0, pady=10)


window = tk.Tk()
window.title("Weather app")

window.columnconfigure(0, weight=1)
window.rowconfigure([0, 5], weight=1)

cityText = tk.Label(text="Type the City:", font=font.Font(size=20))
cityText.grid(row=0, column=0, pady=10)

userinput = tk.Entry()
userinput.grid(row=1, column=0, pady=10)

enterButton = tk.Button(text="Enter", command=getWeather)
enterButton.grid(row=2, column=0, pady=10)
window.mainloop()
