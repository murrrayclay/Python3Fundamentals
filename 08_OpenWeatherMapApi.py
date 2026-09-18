import requests

city = input('Enter city:')
url = 'http://api.weatherapi.com/v1/current.json?key=91d8034b699c4675bbe194800261809&q='+city+'&aqi=no'

response = requests.get(url)
weather_json = response.json()

print(response.status_code)
#print(weather_json)

temperature = weather_json.get('current').get('temp_c')

description = weather_json.get('current').get('condition').get('text')

print('Today weather in ' + city + ' is ' + description + ' and ' + str(temperature) + '°C')
