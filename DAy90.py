import requests
import json

url = (
    "https://newsapi.org/v2/top-headlines?"
    "country=us&"
    "apiKey=b7cfe61b3c3a4217b431a1856c8a0a85"
)

data = requests.get(url).json()

json_object = json.dumps(data, indent=4)

with open("Day90File.json", "w") as outfile:
    outfile.write(json_object)
