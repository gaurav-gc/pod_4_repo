print('test')
from inheritance import *


print('')
print('')
print('')
print('Bus Station 1')
bus1 = BusStation(station_name="la playa", location="on the beach", routes=['tulum', 'cabo', 'mexico'])
# bus1.open_station()
# bus1.close_station()
bus1.show_info()

print('')
print('')
print('')
print('Subway Station 1')
tijuana = SubwayStation(station_name="market st", location = "4th street and market", lines=['A', 'B', 'C', 'D'])
tijuana.show_info()

print('')
print('')
print('')
print('Subway station 2')
frisco = SubwayStation(station_name="twin peaks", location = "soma", lines=['1', '2', '3', '4'])
frisco.show_info()

# when running this page, why is it running both inheritance.py and 09_station_planning.py ?