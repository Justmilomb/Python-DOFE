import requests


API_KEY = "24d1be9d1577492c7b63ea4adfe65877" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name:  ").strip().upper()
params = {"q": city, "appid": API_KEY, "units": "metric" }
response = requests.get(BASE_URL, params = params)
if response.status_code == 200:
	data = response.json()
	temp =  data["main"]["temp"]
	weather = data["weather"][0]["description"]
	humidity = data["main"]["humidity"]
	print(f"Weather in {city}:  ")
	print(f"Temperature:  {temp}")
	print(f"Condition:  {weather.capitalize()}")
	print(f"humidity:  {humidity}%")
else:
	print("Error: API issue...")
