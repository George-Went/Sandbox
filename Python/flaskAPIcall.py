## Ref: https://www.dataquest.io/blog/python-api-tutorial/
# the requests library allows us to make simple REST calls
#%%
from email import header
from os import access
import requests
from requests.auth import HTTPBasicAuth
import json

#%%
## ----------------------------------------------------------------------
## GET login request + header/auth 
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
#%%


## ----------------------------------------------------------------------
## COTAINER DATABASE API 
## ----------------------------------------------------------------------
#%%
print("GET CONTAINER --------------------------------")
api_url = "http://localhost:5000/api/v1/dockerapi/"
headers = {"Authorization":"Bearer "+ access_token}
response = requests.get(api_url, headers=headers)
print(json.dumps(response.json(), indent=1))

#%%
print("GET INDUVIDUAL CONTAINER --------------------------------")
api_url = "http://localhost:5000/api/v1/container/34"
headers = {"Authorization":"Bearer "+ access_token}
response = requests.get(api_url, headers=headers)
print(json.dumps(response.json(), indent=1))

#%%
print("ADDING CONTAINER ---------------------------------")
api_url = "http://localhost:5000/api/create"
## Example Payload with all options
payload = {
    "name": "ApacheServer",
    "image": "httpd",
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
    "name": "Test4",
    "image": "alpine",
}

response = requests.post(api_url, headers=headers, json=test_container) ## use "json" instead of "data" (will format data into json)

print(response.headers)
print(response.json())

#%%
print("UPDATE CONTAINER ---------------------------------")
api_url = "http://localhost:5000/api/v1/container/34"
test_container = {
    "command": "tail -f /dev/null", 
    "name": "Test4_Update",
    "image": "alpine",
}
response = requests.put(api_url, headers=headers, json=test_container)
print(response.content)









#%%

## -------------------------------------------------------------------------------
## DOCKER CLIENT API
## -------------------------------------------------------------------------------
api_url = "http://localhost:5000/api/v1/dockerapi/"
headers = {"Authorization":"Bearer "+ access_token}
response = requests.get(api_url, headers=headers)
print(response.json())

container_ids = {c['name']:c['id'] for c in response.json()['result']}


container_ids = {}

for c in response.json()['result']:
  container_ids[c['name']] = c['id']

#%%
start_result = requests.post(api_url + '/run/' + str(container_ids['Test4']), headers=headers)


print(start_result)

# %%
api_url = "http://localhost:5000/api/v1/dockerapi"
headers = {"Authorization":"Bearer "+ access_token}

restart_result = requests.post(api_url + '/restart/' + str(container_ids['Test4']), headers=headers)
print(restart_result)
print(restart_result.content)

# %%
api_url = "http://localhost:5000/api/v1/dockerapi"
headers = {"Authorization":"Bearer "+ access_token}

stop_result = requests.post(api_url + '/stop/' + str(container_ids['Test4']), headers=headers)
print(stop_result)
# %%
api_url = "http://localhost:5000/api/v1/dockerapi"
headers = {"Authorization":"Bearer "+ access_token}

remove_result = requests.post(api_url + '/remove/' + str(container_ids['Test4']), headers=headers)
print(remove_result)

# %%
headers = {"Authorization":"Bearer "+ access_token}

## SETUP 
api_url = "http://localhost:5000/api/v1/container"

Container1 = {
    "command": "tail -f /dev/null", 
    "name": "Container1",
    "image": "alpine",
}
Container2 = {
    "command": "tail -f /dev/null", 
    "name": "Container2",
    "image": "alpine",
}
Container3 = {
    "command": "tail -f /dev/null", 
    "name": "Container3",
    "image": "alpine",
}
Container4 = {
    "command": "tail -f /dev/null", 
    "name": "Container4",
    "image": "alpine",
}



response = requests.post(api_url, headers=headers, json=Container1) ## use "json" instead of "data" (will format data into json)
response = requests.post(api_url, headers=headers, json=Container2)
response = requests.post(api_url, headers=headers, json=Container3)
response = requests.post(api_url, headers=headers, json=Container4)

print(response.headers)
print(response.json())


#%%
api_url = "http://localhost:5000/api/v1/dockerapi/"
headers = {"Authorization":"Bearer "+ access_token}
response = requests.get(api_url, headers=headers)

container_ids = {c['name']:c['id'] for c in response.json()['result']}
print(container_ids)

#%%
## --------------------------------------------------
## ADD A GROUP
##---------------------------------------------------
api_url = "http://localhost:5000/api/v1/group/add"
headers = {"Authorization":"Bearer "+ access_token}

group1 = {
    "name": "Group1"
}
group2 = {
    "name": "Group2"
}
response = requests.post(api_url, headers=headers, json=group1)
response = requests.post(api_url, headers=headers, json=group2)

api_url = "http://localhost:5000/api/v1/group"
response = requests.get(api_url, headers=headers)

group_ids = {c['name']:c['id'] for c in response.json()['result']}

## ACTION
#%%
##---------------------------------------------------
## ADD CONTAINERS TO GROUPS
##---------------------------------------------------
api_url = "http://localhost:5000/api/v1/group/add_container"
headers = {"Authorization":"Bearer "+ access_token}

data = {"group_id": group_ids['Group1'],
        "container_id": container_ids["Container1"]}

data = {"group_id": 2,
        "container_id": 4}

response = requests.post(api_url, headers=headers, json=data)

data = {"group_id": group_ids['Group1'],
        "container_id": container_ids["Container2"]}

response = requests.post(api_url, headers=headers, json=data)

data = {"group_id": group_ids['Group2'],
        "container_id": container_ids["Container3"]}

response = requests.post(api_url, headers=headers, json=data)

data = {"group_id": group_ids['Group2'],
        "container_id": container_ids["Container4"]}

response = requests.post(api_url, headers=headers, json=data)

## EXPECTED RESULT 
#%%
api_url = "http://localhost:5000/api/v1/group/run/"
headers = {"Authorization":"Bearer "+ access_token}


response = requests.post(api_url + str(group_ids['Group1']), headers=headers)

print(response)
print(response.content)

## 
#%%
api_url = "http://localhost:5000/api/v1/group/stop/"
headers = {"Authorization":"Bearer "+ access_token}


response = requests.post(api_url + str(group_ids['Group1']), headers=headers)

print(response)
print(response.content)

# %%
api_url = "http://localhost:5000/api/v1/group/remove/"
headers = {"Authorization":"Bearer "+ access_token}


response = requests.post(api_url + str(group_ids['Group2']), headers=headers)

print(response)
print(response.content)

# %%
api_url = "http://localhost:5000/api/v1/group/remove_container"
headers = {"Authorization":"Bearer "+ access_token}


response = requests.post(api_url, headers=headers, json=dict(
    group_id = group_ids['Group1'], container_id = container_ids['Container2']))

print(response)
print(response.content)

# %%
api_url = "http://localhost:5000/api/v1/dockerapi/remove"
headers = {"Authorization":"Bearer "+ access_token}

response = requests.post(api_url + "/" + str(container_ids['Container4']), headers=headers)

print(response)
print(response.content)
# %%

print("CREATE CONTAINER ---------------------------------")
api_url = "http://localhost:5000/crucible/api/create2"
test_container = {
    "command": "tail -f /dev/null", 
    "name": "Test5_Update",
    "image": "alpine",
}
response = requests.post(api_url, json=test_container)
print(response.content)



# %%
