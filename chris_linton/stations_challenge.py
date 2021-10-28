'''
NYC Transit Challenge! 

In this challenge, you will use OOP and inheritance to design subway and bus stations!
You'll use the parent class Station to make child classes for SubwayStation and BusStation. 

Note, you should NOT need to change the Station class at all in this challenge.

Since subways and buses have different information, the methods and attributes will be a bit different
'''

print()

print('Question 1: Making the SubwayStation Class')
'''
Using the Station class below as the parent, make a child class called SubwayStation

SubwayStation should:
-have an additional attribute called 'lines' that is user-defined as a list during initialization. 
    this will indicate which subway lines stop at the station (for example ['A', 'C'])
-override the show_info() method from Station to display which subway lines stop there, in addition to the station_name and location
'''
# creates a parent class
class Station:
    # parent class initialization function
    def __init__(self, station_name, location):
        self.station_name = station_name
        self.location = location
    # defines a method that prints station info 
    def show_info(self):
        print(f'{self.station_name} station is located at {self.location}')
# creates a child class of parent class Station
class SubwayStation(Station):
    # child class initialization function
    def __init__(self, station_name, location, lines):
        super().__init__(station_name, location)
        # create an additional user-defined attribute 'lines'
        self.lines = lines
    # defines a method to print subway station info that overrides the same method of the parent class
    def show_info(self):
        # set a variable to the value of the length of the lines list
        lines_len = len(self.lines)
        # set a variable to the value of the last string in the lines list
        last_line = self.lines[lines_len-1]
        # remove the last element of the lines list so when printed can add "and" before it
        self.lines.remove(last_line)
        # join the lines list of string to create one string assigned to a variable
        station_lines = ", ".join(self.lines)
        # add the last element of the lines list back in so that the list remains the same after the method is called
        self.lines.append(last_line)
        print(f'{self.station_name} station is located at {self.location}. The subway lines {station_lines}, and {last_line} stop at this location.')

print()

print('Question 2: Make an example subway station')
'''
Using your SubwayStation class, instantiate a subway station with the info below. 
Then run the show_info() method to make sure you get the station_name, location, and lines printed out

station_name: '14th street'
location: '14th street and 7th avenue'
lines: ['1', '2', '3', 'L']
'''

# instantiate a SubwayStation object
subway_station = SubwayStation(station_name='14th street', location='14th street and 7th avenue', lines=['1', '2', '3', 'L'])
# call SubwayStation method to show station info
subway_station.show_info()

print()

print('Question 3: Making the BusStation Class')

'''
Using the Station class below as the parent, make a child class called BusStation

BusStation should:
-have an additional attribute called 'routes' that is user-defined as a list during initialization. 
    this will indicate where buses can go from this station. For example, ['DC', 'Philly', 'Pittsburgh']
-have an additional attribute called 'open' that is always initalized as True (a boolean variable)
-have additional methods called open_station() and close_station() to open and close the station
-override the show_info() method from Station to display the bus routes and if the station is open, in addition to the station name and location
'''
# creates a child class of parent class Station
class BusStation(Station):
    # child class initialization function
    def __init__(self, station_name, location, routes):
        super().__init__(station_name, location)
        # create an additional user-defined attribute 'routes'
        self.routes = routes
        # create an additional attribute 'open' intitialized to True
        self.open = True
    # defines a method that changes attribute value to True, meaning the station is open
    def open_station(self):
        self.open = True
    # defines a method that changes attribute value to False, meaning the station is closed
    def close_station(self):
        self.open = False
    # defines a method to print bus station info that overrides the same method of the parent class
    def show_info(self):
        # set a variable to the value of the length of the routes list
        routes_num = len(self.routes)
        # set a variable to the value of the last string in the routes list
        last_route = self.routes[routes_num-1]
        # remove the last element of the routes list so when printed can add "and" before it
        self.routes.remove(last_route)
        station_routes = ", ".join(self.routes)
        self.routes.append(last_route)
        # conditional to check if station is open
        if self.open:
            print(f'{self.station_name} station is located in {self.location}. This station that services bus routes to {station_routes}, and {last_route} is currently open.')
        # conditional that runs if station is closed
        else:
            print(f'{self.station_name} station is located in {self.location}. This station that services bus routes to {station_routes}, and {last_route} is currently closed.')

print()

print('Question 4: Make an example bus station')
'''
Using your BusStation class, instantiate a bus station with the info below. 
Then, run the show_info() method to make sure you get the station_name, location, routes, and whether the station is open printed out
Then, demonstrate that you can close and open the bus station
    i.e. that the show_info() method reflects correctly when the station is open versus closed

station_name: 'NYC Megabus Stop'
location: '34th street and 12th avenue'
lines: ['Boston', 'DC', 'Philly']
'''

# instantiate a BusStation object
bus_station = BusStation(station_name='NYC Megabus Stop', location='34th street and 12th avenue', routes=['Boston', 'DC', 'Philly'])
# call BusStation method to show station info
bus_station.show_info()
# call BusStation method to close station
bus_station.close_station()
# call BusStation method to show station info
bus_station.show_info()
# call BusStation method to open station
bus_station.open_station()
# call BusStation method to show station info
bus_station.show_info()

print()

print('Question 5: Importing your classes')
print()

'''
Now, it's time to design a few more stations of your own in another script! 

Make a new python script called "station_planning.py"
    -In this script, *import* the classes you made in this challenge file
    -Instantiate 3 more stations of your choosing (at least 1 bus and 1 subway)
    -Feel free to make up names, locations, lines, and routes!
'''

