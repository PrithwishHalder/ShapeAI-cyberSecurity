import requests

from datetime import datetime

print("\n********** Weather App **********\n")

api_key = '039e099f1f9916bb7cb717eba3504d85'
location = input("Enter the Name of the City : ")

url = 'https://api.openweathermap.org/data/2.5/weather?q='+location+"&appid="+api_key

# Getting the response and converting the data in JSON

response = requests.get(url)
data = response.json()

temp_city = (data['main']['temp'] - 273.15)
min_temp = (data['main']['temp_min'] - 273.15)
max_temp = (data['main']['temp_max'] - 273.15)
weather_details = str(data['weather'][0]['description']).upper()
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind_speed = data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

temp = "Current Temperature : {:.2f} \N{DEGREE SIGN}C".format(temp_city)
temp_min = "Min Temperature : {:.2f} \N{DEGREE SIGN}C".format(min_temp)
temp_max = "Max Temperature : {:.2f} \N{DEGREE SIGN}C".format(max_temp)

# Structuring the data

details = '''{} \n{} \n{} \n
Current Weather Description : {} 
Humidity : {} % 
Pressure : {} mb 
Current Wind Speed : {} kmph
'''.format(temp, temp_min, temp_min, weather_details, humidity, pressure, wind_speed)

# Printing weather details in terminal

print('''\n------------- WEATHER STATS -------------
{} || {}
-----------------------------------------\n
{}
'''.format(location.upper(), date_time, details))

# Writing weather details in Weather.txt file

f = open("Weather.txt", "w")
f.write("Current Weather Report : \n------------------------------------\n")
f.write("\nLocation : "+location.upper())
f.write("\nWeather : "+weather_details)
f.write("\nTime : "+date_time)
f.write("\n\n"+details)
f.close()
