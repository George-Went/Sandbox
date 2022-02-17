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
print("selecting a specific container")
client = docker.from_env()
for container in client.containers.list():
    print(container.name)

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
    "detach": True
}

print("creating a container from an object / dictionary")
print(containerObject["name"])
client = docker.from_env()
container = client.containers.run(containerObject["image"], detach=containerObject["detach"])

## Making sure we dont delete portainer
client = docker.from_env()
container = client.containers.get("portainer")
print("got container: " + str(container))
print("also known as: " + str(container.name))

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
    

    
        
