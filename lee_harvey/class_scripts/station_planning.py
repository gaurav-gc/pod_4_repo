from stations_challenge import *

bryant_park = SubwayStation('42nd Street–Bryant Park/Fifth Avenue', '42nd Street & Fifth Avenue', ['B', 'D', 'F', 'M'])
herald_square = SubwayStation('34th Street–Herald Square', '34th Street & Sixth Avenue', ['B', 'D', 'F', 'M', 'N', 'Q', 'R', 'V'])
grand_central = SubwayStation('Grand Central Station', '42nd Street & Park Avenue', ['4', '5', '6', '7', 'S'])
port = BusStation('Port Authority Bus Terminal', '625 8th Ave', ['Red', 'Blue', 'Yellow', 'Orange'])

port.close_station()
bryant_park.show_info()
print()
herald_square.show_info()
print()
grand_central.show_info()
print()
port.show_info()