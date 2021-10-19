from stations_challenge_solutions import *

nostrand = SubwayStation(station_name = 'Nostrand Ave', 
    location= "Nostrand Avenue & Fulton Street", 
    lines = ['A', 'C'])

jackson = SubwayStation(station_name='Jackson Heights–Roosevelt Avenue/74th Street station', 
    location='Roosevelt Avenue, 74th Street, and Broadway', 
    lines = ['7', 'E', 'F', 'M', 'R'])

port_authority = BusStation(station_name = 'Port Authority', 
    location = 'Times Square', 
    routes = ['DC', 'Providence', 'Baltimore'])



nostrand.show_info()
jackson.show_info()
port_authority.show_info()

# test out closing/opening port authority
port_authority.close_station()
port_authority.show_info()
port_authority.open_station()
port_authority.show_info()
