# import classes and their methods from stations_challenge.py
from stations_challenge import SubwayStation, BusStation

# instantiate a BusStation object
bus_station1 = BusStation(station_name='Park Ave', location='New York City', routes=['Albany', 'Buffalo', 'Hoboken'])
# instantiate a BusStation object
bus_station2 = BusStation(station_name='Capital', location='Albany', routes=['Ithaca', 'Buffalo', 'Syracuse'])
# instantiate a SubwayStation object
subway_station1 = SubwayStation(station_name='Union Square', location='7th Ave & Filmore', lines=['A', 'B', 'C'])
# instantiate a SubwayStation object
subway_station2 = SubwayStation(station_name='Times Square', location='Broadway & 5th Ave', lines=['C', 'D', 'E'])

# call BusStation method to show station info
bus_station1.show_info()
print()
# call BusStation method to close station
bus_station2.close_station()
# call BusStation method to show station info
bus_station2.show_info()
print()
# call SubwayStation method to show station info
subway_station1.show_info()
print()
# call SubwayStation method to show station info
subway_station2.show_info()

print()