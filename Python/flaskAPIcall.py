## Ref: https://www.dataquest.io/blog/python-api-tutorial/
# the requests library allows us to make simple REST calls
from os import access
import requests
from requests.auth import HTTPBasicAuth
import json


## ----------------------------------------------------------------------
## GET login
## ----------------------------------------------------------------------
print("GET LOGIN DETAILS")
api_url = "http://localhost:5000/api/v1/security/login"

payload = {
  "password": "admin",
  "provider": "db",
  "refresh": 'true',
  "username": "admin"
}

response = requests.post(api_url, json=payload).json() ## formats the response as a json 
print(response)
print(response['access_token']) ## prints only the access token from the response json 


access_token = response['access_token']

## ----------------------------------------------------------------------
## GET request + header/auth 
## ----------------------------------------------------------------------
print("GET CONTAINERS --------------------------------")
api_url = "http://localhost:5000/api/v1/dockerapi/"
headers = {"Authorization":"Bearer "+ access_token}
response = requests.get(api_url, headers=headers)
print(response.json)





## ------------------------------------------------
## Requesting web pages with POST json parameters 
## ------------------------------------------------
## json parameters 
print("ADDING CONTAINER ---------------------------------")
api_url = "http://localhost:5000/api/v1/container"
payload = {
    "name": "Test3",
    "image": "alpine",
    "command": "entrypoint.sh",
    "environment": "TEST=test",
    "entrypoint": "entrypoint.sh",
    "network": "test",
    "network_mode": "Host",
    "ports": "8081/tcp",
    "restart_policy": "Always",
    "volumes": "/test:/test"
}

test_container = {
    "command": "tail -f /dev/null", 
    "entrypoint": "entrypoint.sh",
    "environment": ["ENV: Test", "ENV2: Test"],
    "name": "Test3",
    "image": "alpine",
    "network": "test",
    "network_mode": "bridge",
    "ports": [{"8080/tcp": 8080}],
    "restart_policy": {"Name": "always", "MaximumRetryCount": 1},
    "volumes": [".:/test"]
}


response = requests.post(api_url, headers=headers, json=test_container) ## use "json" instead of "data" (will format data into json)

print(response.headers)
print(response.json)

# response = requests.post("http://localhost:5000/api/v1/dockerapi/run", params=parameters)

# json_print(response.json())



