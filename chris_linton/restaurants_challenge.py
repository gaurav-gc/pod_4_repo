print("Challenge: Favourite Restaurants")

print()

print("Question 1")
print()

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)
print()

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print('Four Barrel Coffee Coordinates:', 'latitude', restaurant['latitude'], '&', 'longitude', restaurant['longitude'])
print()
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(f"Four Barrel Coffee Address: {restaurant['address1']},  {restaurant['city']}, {restaurant['state']} {restaurant['zip_code']}")
print()
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print('Four Barrel Coffee Website:', restaurant['url'])


print()

print("Question 2")
print()

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)
favourite_restaurant1 = {
    "name": "Liberty Market",
    "address": "1075 Gilbert Ave, Gilbert, AZ 85224",
    "favourite_dish": "Elote Pizza"
    }
favourite_restaurant2 = {
    "name": "Uncle Sal's",
    "address": "375 Hayden Dr, Scottsdale, AZ 85264",
    "favourite_dish": "Lobster Ravioli"
    }
favourite_restaurant3 = {
    "name": "Flaming Kabobs",
    "address": "652 Baseline Dr, Mesa, AZ 85210",
    "favourite_dish": "Gyro Platter"
    }
# TODO: Print each dictionary
print(f"Restaurant1:\n {favourite_restaurant1}\n Restaurant2:\n {favourite_restaurant2}\n Restaurant3:\n {favourite_restaurant3}")


# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''

print()

print("Question 3")
print()
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
favourite_restaurant1.pop('favourite_dish')
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
print(favourite_restaurant1)

print()

print("Question 4")
print()
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
favourite_restaurant2['address'] = '98 Scottsdale Blvd, Scottsdale, AZ 85264'
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
print(favourite_restaurant2['address'])
# TODO: Print the updated dictionary.

print()
