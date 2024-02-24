import tkinter as tk
from tkinter import messagebox
import requests

def fetch_weather():
    city_name = city_entry.get()
    api_key = "ca8bf9db74ae4abc801181715242302" 
    
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city_name,
        "aqi": "no"
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        weather_description = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]
        
        messagebox.showinfo("Weather", f"Location: {location}\nWeather: {weather_description}\nTemperature: {temperature}°C")
    else:
        messagebox.showerror("Error", "Failed to fetch weather data!")

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

root.mainloop()
