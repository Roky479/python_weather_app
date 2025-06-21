import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not city.strip():
        messagebox.showwarning("Input error", "City name cannot be empty!")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        display_weather(data)
    elif response.status_code == 404:
        messagebox.showerror("Error", f"City '{city}' not found.")
    else:
        messagebox.showerror("Error", f"Failed to fetch weather.\nStatus code: {response.status_code}")

def display_weather(data):
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

    result = (
        f"Weather in {data['name']}, {data['sys']['country']}:\n"
        f"🌡 Temperature: {data['main']['temp']}°C\n"
        f"🌥 Description: {data['weather'][0]['description'].capitalize()}\n"
        f"💧 Humidity: {data['main']['humidity']}%\n"
        f"💨 Wind Speed: {data['wind']['speed']} m/s\n"
        f"🔽 Pressure: {data['main']['pressure']} hPa\n"
        f"🌅 Sunrise: {sunrise}\n"
        f"🌇 Sunset: {sunset}"
    )
    weather_text.delete(1.0, tk.END)
    weather_text.insert(tk.END, result)

# Setup Tkinter window
root = tk.Tk()
root.title("Python Weather App")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Enter city (or city,country code):")
label.pack()

city_entry = tk.Entry(frame, width=30)
city_entry.pack()
city_entry.focus()

button = tk.Button(frame, text="Get Weather", command=lambda: get_weather(city_entry.get()))
button.pack(pady=5)

weather_text = tk.Text(frame, height=10, width=50)
weather_text.pack()

root.mainloop()