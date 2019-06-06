import requests

api_url = 'http://shibe.online/api/shibes?count=1'

params = {"count": 10}

response = requests.get(api_url, params=params)

status_code = response.status_code

print('status code: ', status_code)

json_data = response.json()

print(type(json_data))

print(json_data)
