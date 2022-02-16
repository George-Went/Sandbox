from calendar import c
from os import name
import docker

## Examples of using python to interact with the docker api


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


## Creating / Running docker containers from existing images
# print("creating contianers")
# client = docker.from_env()
# # client.containers.run(image, command)
# container = client.containers.run("ubuntu:latest", "echo hello world")

## Run a container in the background
# print("running containers in the background")
# client = docker.from_env()
# container = client.containers.run("bfirsh/reticulate-splines", detach=True)

listContainer()

## Selecting a specific container 
print("selecting a specific container")
client = docker.from_env()
print(client.containers.list())
for i in client.containers.list():
    print(i)
    # container = client.containers.list()[i]
    print(container)

# container = client.containers.get()[0]
# print(container)

array = ["cat", "dog", "rabbit"]
print(array)
print(array[1])

for i in array:
    print(i)


# ## Stopping all containers
# print("stopping all the containers (this shouldn't be running)") 
# client = docker.from_env()
# for container in client.containers.list():
#   container.stop()