import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = 'jsoncbv/'

resp1 = requests.get(BASE_URL+ENDPOINT)
resp2 = requests.post(BASE_URL+ENDPOINT)
resp3 = requests.put(BASE_URL+ENDPOINT)
resp4 = requests.delete(BASE_URL+ENDPOINT)
print(resp1.json())
print(resp2.json())
print(resp3.json())
print(resp4.json())
