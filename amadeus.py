
import urllib.request
import requests
import amadeus
import sys
import certifi
import re
import ast

from amadeus import Flights

# if sys.argv[1] is None or sys.argv[2] is None:
#     print("Usage: python main.py <latitude> <longitude>")

if len(sys.argv) < 3:
    print("Usage: python main.py <latitude> <longitude>")
    exit()

# trial: python main.py 42.407467 -71.276749
lat = sys.argv[1]
lon = sys.argv[2]

lat = str(lat)
lon = str(lon)

link = 'https://api.sandbox.amadeus.com/v1.2/airports/nearest-relevant?apikey=YOY6pU9JGlYtaMjIzylgt92t00ROtFle&latitude=' + lat + '&longitude=' + lon

response = requests.get(link, verify=True)
response = response.content.decode("utf-8")
response = ast.literal_eval(response)

print()
for i in range(0, len(response)):
    print("Airport: " + response[i]['airport_name'])
    print("City: " + response[i]['city_name'])
    print("Distance: " + str(response[i]['distance']))
    print()



# flights = Flights('YOY6pU9JGlYtaMjIzylgt92t00ROtFle')
# rails = RailStations('YOY6pU9JGlYtaMjIzylgt92t00ROtFle')

# # random place to go to
# resp = flights.inspiration_search(
#     origin='BKK',
#     departure_date="2018-06-20--2018-06-27",
#     max_price=10000)
# print(resp)

# Auto-complete: matches airports from airport ticker
# resp = flights.auto_complete(term=sys.argv[1])

# for i in range(0, len(resp)):
    # if resp[i]['label'] == 'Columbus Airport [CSG]':
        # print(resp[i])

# print("possible values:")
# for i in range(0, len(resp)):
#     print(resp[i]['value'], end=" ")

# for i in range(0, len(resp)):
#     if resp[i]['value'] == sys.argv[1]:
#         print(resp[i]['label'])


# # Auto-complete: matches railstations from railstation ticker
# resp = rails.auto_complete(term='VENT')





