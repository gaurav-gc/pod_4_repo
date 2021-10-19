'''
NYC Transit Challenge!

In this challenge, you will use OOP and inheritance to design subway and bus stations!
You'll use the parent class Station to make child classes for SubwayStation and BusStation.

Note, you should NOT need to change the Station class at all in this challenge.

Since subways and buses have different information, the methods and attributes will be a bit different
'''


print('Question 1: Making the SubwayStation Class')
'''
Using the Station class below as the parent, make a child class called SubwayStation

SubwayStation should:
-have an additional attribute called 'lines' that is user-defined as a list during initialization.
    this will indicate which subway lines stop at the station (for example ['A', 'C'])
-override the show_info() method from Station to display which subway lines stop there, in addition to the station_name and location
'''


class Station:
    def __init__(self, station_name, location):
        self.station_name = station_name
        self.location = location

    def show_info(self):
        print(f'{self.station_name} station is located at {self.location}')


apples = Station("Wilson Ave", "Brooklyn")
print(apples.station_name)
# --> Wilson Ave.
# --> self.station_name = apples.station_name

oranges = Station("Union Sq.", "NYC")
print(oranges.station_name)
# --> Union Sq.
# --> self.station_name = oranges.station_name

grapes = Station("Atlantic Ave", "Brooklyn")
print(grapes.station_name)
# --> Atlantic Ave.
# --> self.station_name = grapes.station_name
oranges.station_name
apples.station_name


# Step 1) in order to create a class you need the keyword class
# --> class SubwayStation():

# Step 2) in order to create a child class of Station passed 'Station' in SubwayStation(Station)
# SubwayStation will now inherit methods and attributes of Station
# --> class SubwayStation(Station):
# class SubwayStation(Station):
#    pass

# Step 3) Inheritance
#s1 = SubwayStation("Union Sq", "NYC")
# s1.show_info()
# --> Union Sq station is located at NYC"
# print(s1.station_name)
# --> Union Sq

class SubwayStation(Station):
    def __init__(self, station_name, location, lines=list):
        super().__init__(station_name, location)
        self.lines = lines

    def show_info(self):
        print(
            f'{self.station_name} station is located at {self.location} and it has {self.lines}')


subStat1 = SubwayStation(
    '14th Street', '14th street and 7th avenue', ['1', '2', '3', 'L'])

# OBJECTS --> 'special powers' == specific functionality
# Methods are Functions --> Methods are tied to a specific object
# lists
list1 = ["a", "a"]
# list1.
# dictionaries
dict1 = {}
dict1.pop()
# strings
str1 = ""
# str1.
# floats
float1 = 1.0
# float1.
# tuples
#tuple1 = (str1, float1)
# classes

# parameters are passed through during function definition


def sampleFunction(str1, str2):
    print(f'{str1} and {str2}')


# arguments are passed through during calling of function
sampleFunction('apples', 'oranges')

print('Question 2: Make an example subway station')
'''
Using your SubwayStation class, instantiate a subway station with the info below.
Then run the show_info() method to make sure you get the station_name, location, and lines printed out

station_name: '14th street'
location: '14th street and 7th avenue'
lines: ['1', '2', '3', 'L']
'''
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
print('Question 5: Importing your classes')

'''
Now, it's time to design a few more stations of your own in another script! 

Make a new python script called "station_planning.py"
    -In this script, *import* the classes you made in this challenge file
    -Instantiate 3 more stations of your choosing (at least 1 bus and 1 subway)
    -Feel free to make up names, locations, lines, and routes!
'''
