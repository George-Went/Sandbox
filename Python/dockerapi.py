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
