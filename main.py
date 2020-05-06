import requests
import json

city = input('What city do you want the weather for\n')


url = "http://api.openweathermap.org/data/2.5/weather?appid=31d821089af2366c1c6766f97cd88ea6&q={}&units=imperial".format(city)

weather = requests.get(url).json()

name = weather['name']
desc = weather['weather'][0]['description']
temp = weather['main']['temp']
wind = weather['wind']['speed']

final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s \nWind speed: %s ' % (name, desc, temp, wind)

print(final_str)