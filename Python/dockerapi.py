from calendar import c
from os import name
import docker

## Examples of using python to interact with the docker api

## VIEWING EXISTING CONNTAINERS AND IMAGES
print("Container List")
client = docker.from_env()
for container in client.containers.list():
    print(container)  # Prints containers induvidually
print(client.containers.list())  # Prints containers in a array

print("Container List v2")
client = docker.from_env()
for container in client.containers.list():
    print(container.id)

def listContainer():
    print("Container List v3")
    result = []
    for container in client.containers.list():
        result.append(
            {
                "id": container.id,
                "name": container.name,
                "image": container.image,
            }
        )
    print(result)

## Getting Docker Images
print("Image List")
client = docker.from_env()
for image in client.images.list():
    print(image.id)
print(client.images.list(name))

print("Image List v2 ")
client = docker.from_env()
for image in client.images.list():
    print(image.tags)
print(client.images.list(name))

## Getting container names
#%%
print("selecting a specific container")
client = docker.from_env()
for container in client.containers.list():
    print("Container: " + container.name)
# %%

## Selecting a specific container 
client = docker.from_env()
for container in client.containers.list():
    if container.name == "admiring_dewdney":
        print("container exists")

## selecting a specific container v2 - including error handeling! 
client = docker.from_env()
try:     
    container = client.containers.get("jovial_cannon")
    print("got container: " + str(container))
    print("also known as: " + str(container.name))
except:
    print("no container named jovial_cannon")

## Selecting containers other than a specific container
client = docker.from_env()
for container in client.containers.list():
    if container.name != "portainer" or "crucible_db_1":
        print("container is not portainer or crucible")





## CREATING NEW CONTAINERS 

## Creating / Running docker containers from existing images
# print("creating contianers")
# client = docker.from_env()
# # client.containers.run(image, command)
# container = client.containers.run("ubuntu:latest", "echo hello world")

## Run a container in the background
print("running containers in the background")
client = docker.from_env()
container = client.containers.run("bfirsh/reticulate-splines", detach=True)

## Creating a container from an object / dictionary 
containerObject = {
    "name": "docker_from_object",
    "image": "bfirsh/reticulate-splines",
    "ports": [{'8080/tcp': 8080}],
    "detach": True
}

print("creating a container from an object / dictionary")
print(containerObject["name"])
client = docker.from_env()
container = client.containers.run(**containerObject["image"], containerObject["ports"], detach=containerObject["detach"])




## Making sure we dont delete portainer
client = docker.from_env()
container = client.containers.get("portainer")
print("got container: " + str(container))
print("also known as: " + str(container.name))

#%%
import docker
## MODIFYING EXISTING CONTAINERS
print("stopping existing containers")
client = docker.from_env()
print(client.containers.list())
for container in client.containers.list():
    print(str(container.name) + "   " + str(container.image))
    if container.image != "portainer/portainer-ce" or "crucible_db_1":
        print("stopping container: " + container.name)
        container.stop()
    else: 
        print("hey this is the portainer container, dont stop it") 
    

    
        

# %%
## Checks if container exists and stops a container based on its name 
for container in client.containers.list(all=True):
    if container.name == "Test6":
        print("Test 6 exists")
        container.stop()
    else:
        print("No container with ")
# %%
import docker
docker_client = docker.from_env()

pretend_JSON = {
    "name": "Container1",
    "command": "entrypoint.sh",
    "entrypoint": "entrypoint.sh",
    "environment": ["TEST=test"],
    "image": "alpine",
    "network": "containerNetwork1",
    "network_mode": "bridge",
    "ports": ["8080/tcp","8080"],
    "restart_policy": "Always",
    "volumes": [ "/test:/test"]
}


print(pretend_JSON)

# Ports are stored in the database a as a array so we have to turn it into a object
port_list = []
for x in pretend_JSON['ports']:
    port_list.append(x)
print(port_list)

# Create container object to send back to frontend
containerObject = {
    "image": pretend_JSON['image'],
    "command": pretend_JSON['command'],
    "environment": pretend_JSON['environment'],
    "name": pretend_JSON['name'],
    "network": pretend_JSON['network'],
    "ports": port_list,
    "volumes": pretend_JSON['volumes'],
    "detach": True
}
print("CONTAINER OBJ")   
print(containerObject)
print(containerObject["ports"])

docker_client.containers.run(containerObject)

## Creating a container from an object / dictionary 
containerObject = {
    "name": "docker_from_object",
    "image": "bfirsh/reticulate-splines",
    "ports": [{'8080/tcp': 8080}],
    "detach": True
}

print("creating a container from an object / dictionary")
print(containerObject["name"])
client = docker.from_env()
container = client.containers.run(containerObject["image"],containerObject["ports"],detach=containerObject["detach"])


# %%

# %%



## Flask stuff






## ------------------------------------------------------------------------------------------- 
## Docker API Interaction
## -------------------------------------------------------------------------------------------


# List Local Containers
@crucible.route('/api/list', methods=['GET','POST'])
def listContainers():
    print("Container List")
  
    result = []
    for container in dockerClient.containers.list(all=True):
        result.append(
            {
                "id": container.id,
                "name": container.name,
                "image": container.image,
                "status": container.status
            }
        )
    return render_template('crucible/api.html', result = result)

## Test Functions

# Create Local Container
@crucible.route('/api/create', methods=['POST'])
def createContainerAPI():


    print("got request")
    if request.method == 'POST':
        try:
            payload = request.get_json() 
            dockerClient.containers.create(**payload)
            response = {
                    "status": 200, 
                    "message": "container :" + payload["name"] + " is being created"
                }
            print(response)
            return response
        # Error handeling for the docker API
        except errors.APIError as error:
            response = {
                    "status": 400, 
                    "message": "container " + payload["name"] +" was not created",
                    "error": str(error)
                }
            print(response)
            return response
    


# Start Local Container
@crucible.route('/api/start', methods=['POST'])
def startContainer2():
    
    print("got request")
    if request.method == 'POST':
        try:
            payload = request.get_json() 
            container = dockerClient.containers.get(payload['name'])
            container.start()

            response = {
                    "status": 200, 
                    "message": "container :" + payload["name"] + " is starting"
                }
            print(response)
            return response
        # Error handeling for the docker API
        except errors.APIError as error:
            response = {
                    "status": 400, 
                    "message": "container was not created",
                    "error": str(error)
                }
            print(response)
            return response
    


# Create local container from API payload 
@crucible.route('/api/create/<int:id>', methods=['GET','POST'])
def createContainer2(id):
    payload = request.json
    print(payload)



    containerObject = {
        "image": payload["image"],
        "name": payload["name"],
        "command": payload["command"],
        "detach": True
    }
    dockerClient.containers.create(**containerObject)


    response = containerObject
    
    return response

# Start Local Container
@crucible.route('/api/start', methods=['GET','POST'])
def startContainerAPI():
    containerObject = {
        "image": "bfirsh/reticulate-splines",
        "name": "docker_from_object",
        "ports": {'8080/tcp': 8080, '8443/tcp':8443},
        "detach": True
    }

    container = dockerClient.containers.get(containerObject['name'])
    container.start()

    text = "starting container: " + containerObject["name"]

    return render_template('crucible/api.html', result = text)

# Stop Local Container 
@crucible.route('/api/stop', methods=['GET','POST'])
def stopContainerAPI():

    containerObject = {
        "image": "bfirsh/reticulate-splines",
        "name": "docker_from_object",
        "ports": {'8080/tcp': 8080, '8443/tcp':8443},
        "detach": True
    }

    container = dockerClient.containers.get(containerObject['name'])
    container.stop()

    text = "stopping contianer: " + containerObject["name"]
    # client.containers.run(**containerObject)
    # for container in client.containers.list():
    #     if container.name == name:
    #         container.stop()

    return render_template('crucible/api.html', result = text)

# Stop container based on payload
