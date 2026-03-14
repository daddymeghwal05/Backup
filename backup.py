import requests
import json

url = "https://users-f628d-default-rtdb.asia-southeast1.firebasedatabase.app/.json"

data = requests.get(url).json()

with open("backup.json", "w") as f:
    json.dump(data, f, indent=2)
