import json
import requests
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Number of posts:", len(data))
    print("\nFirst post:\n")
    print(json.dumps(data[1], indent=4))
else:
    print("Error:", response.status_code)