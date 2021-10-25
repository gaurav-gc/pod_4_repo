from stations_challenge import *

timesSquare = SubwayStation(station_name = 'Times Sq - 42 St', 
    location= "Times Square", 
    lines = ['IRT 42nd Street Shuttle'])

fultonStreet = SubwayStation(station_name='Fulton Street Subway Station', 
    location='Fulton Street between Broadway &, Nassau St', 
    lines = ['IND Fulton Street Line'])

bolt = BusStation(station_name = 'Bolt Bus Station 1st Avenue And 38th St', 
    location = '676-680 1st Ave', 
    routes = ['Boston'])



timesSquare.show_info()
fultonStreet.show_info()
bolt.show_info()

# test out closing/opening port authority
bolt.close_station()
bolt.show_info()
bolt.open_station()
bolt.show_info()