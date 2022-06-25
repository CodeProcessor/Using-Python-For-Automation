import requests

base_url = "https://api.upcitemdb.com/prod/trial/lookup"

params = {
    "upc": "028914233055"
}

response = requests.get(base_url, params=params)
print(response.url)

info = response.json()

item = info['items'][0]

title = item['title']
brand = item['brand']

print(type(info))

print(title)
print(brand)
