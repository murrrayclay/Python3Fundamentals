import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
#print(json)

print(response.status_code)

print(f"Allow Header: {response.headers.get('Allow')}")

print(json['message'])
print(json['number'])
print('People in space are:')

for person in json['people']:
    print(person['name'])
