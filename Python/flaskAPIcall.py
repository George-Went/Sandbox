# the requests library allows us to make simple REST calls
import requests

r = requests.get("http://localhost:5000/api/v1/container")
# This gives 401 (unauthaurised)

print(r)
