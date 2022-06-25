import requests

key = "492d8461a903868b22ed5b12c8863d10"

lat = "80.0814"
lon = "6.8978"

url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": key
}

response = requests.get(url, params=parameters)
# url_with_params = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
# response = requests.get(url_with_params)

print(response.json())
print(response.url)
