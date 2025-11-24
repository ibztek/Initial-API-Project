import requests
import json

API_KEY = "825877b7d897f111b88ff3d21ba2b840"
city = "London"

url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid=825877b7d897f111b88ff3d21ba2b840"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Number of posts:", len(data))
    print("\nFirst post:\n")
    print(json.dumps(data, indent=4))
else:
    print("Error:", response.status_code)