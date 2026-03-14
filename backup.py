import requests
import json
import os
from datetime import datetime

url = "https://users-f628d-default-rtdb.asia-southeast1.firebasedatabase.app/.json"

data = requests.get(url).json()

# backup folder
folder = "backups"
os.makedirs(folder, exist_ok=True)

# filename with time
filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")

path = os.path.join(folder, filename)

with open(path, "w") as f:
    json.dump(data, f, indent=2)

# keep only last 5 backups
files = sorted(os.listdir(folder))
if len(files) > 5:
    for file in files[:-5]:
        os.remove(os.path.join(folder, file))
