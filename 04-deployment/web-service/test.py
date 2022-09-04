import json
import requests

ride = {
    "PUlocationID": 10,
    "DOlocationID": 50,
    "trip_distance": 40
}

url = "http://localhost:9696/predict"
resp = requests.post(url, json=ride)
print(resp.json())
