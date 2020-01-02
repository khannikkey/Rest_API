import json
import requests
BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def get_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
def get_All():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

def create_Resource():
    new_emp={
    'eno':600,
    'ename':"Vishakha",
    'esal':20000,
    'eaddr':'Banglore',
    }
    resp= requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_Resource()
