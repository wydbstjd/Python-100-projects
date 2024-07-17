import requests
from datetime import datetime

USERNAME = "'''"
TOKEN = "'''"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# https://pixe.la/v1/users/youpig0710/graphs/graph1.html

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "15"
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

pixel_update_data = {
    "quantity" : "30"
}

# response = requests.put(url=update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)