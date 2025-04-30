# import library
import requests
import json
import datetime
from lib_version1 import *

# Output data from API open-gismeteo
lat = 13.41 
lon = 52.52
access_key = "76693f58-e095-4019-8d8e-4fabd40381c8"

headers = {
    "X-Yandex-Weather-Key": access_key
}

query = """{
  weatherByPoint(request: { """ + f"lat: {lat}, lon: {lon}" + """ }) {
    now {
          temperature, 
          humidity, 
          pressure, 
          precType,
          precStrength,
          windSpeed, 
          windDirection
      }
    }
  }"""

response = requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query})

print(response.content)

timestop= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"data_{timestop}.txt"
f = open(f"/home/lisuin/data_yandex/{file_name}", 'wb+')
f.write(response.content)
 
# Connect to PostgreSQL
host = "127.0.0.1"
user = "lisuin"
password = "********"
database = "*******"
port = 5432

command  = SQL_connect(user, password, database, port, host)
connection, cursor = command.PostgreSQL_connect()

print('cursor: ', cursor)

# Insert data to DB
for i in range(0, 23):
    com = SQL_request_INSERT(['', '', '', data['time'][i], data['temperature_2m'][i], data['relative_humidity'][i], data['surface_pressure'][i], (data['wind_speed_10m'][i], data['wind_direction_10m'][i], data['wind_gusts_0m'][i]), data['precipitation'][i], ''], connection, cursor)
    com.CreateNewWeather()
