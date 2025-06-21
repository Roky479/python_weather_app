# Python Weather App

A simple Python application that fetches and displays current weather information for any city using the OpenWeather API.

## Features

- Search weather by city name (supports city,country code like `Paris,FR`)
- Shows temperature, weather description, humidity, wind speed
- Displays additional details like sunrise, sunset, and pressure
- Handles errors for invalid city names or empty input

## How to Use

1. Clone the repo or download the files.
2. Get your free API key from [OpenWeather](https://openweathermap.org/api).
3. Create a `.env` file in the project folder and add your API key:
4. Install dependencies:

```bash
pip install -r requirements.txt

python weather.py

Enter city name: London,GB

Weather in London, GB:
🌡 Temperature: 15°C
🌥 Description: Clear sky
💧 Humidity: 56%
💨 Wind Speed: 3.5 m/s
🌅 Sunrise: 06:30 AM
🌇 Sunset: 07:45 PM
🌡 Pressure: 1012 hPa
