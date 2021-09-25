print("Challenge: Favourite Restaurants")

print()

print("Question 1")

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

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print(f"The latitude and longitude of Four Barrel Coffee, respectively is, {restaurant['latitude']}, {restaurant['longitude']}.")
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(f"You can visit Four Barrel Coffee at {restaurant['address1']} {restaurant['city']}, {restaurant['state']} {restaurant['zip_code']} {restaurant['country']}.\n")
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(f"Visit Four Barrel Coffee online @ {restaurant['url']}.\n")

print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)
nyc_restaurant_1 = {
    'name' : 'Crown Shy',
    'address' : '70 Pine St.',
    'city' : 'New York',
    'state' : 'New York',
    'zip_code' : 10005,
    'favorite_dish' : 'guyere fritters',
    'url' : 'http://www.crownshy.nyc'
}

nyc_restaurant_2 = {
    'name' : 'Sushi Nakazawa',
    'address' : '23 Commerce St.',
    'city' : 'New York',
    'state' : 'New York',
    'zip_code' : 10004,
    'favorite_dish' : 'dungeness crab',
    'url' : 'http://www.sushinakazawa.com'
}

nyc_restaurant_3 = {
    'name': 'Lillo',
    'address' : '331 Henry St.',
    'city' : 'Brooklyn',
    'state' : 'New York',
    'zip_code' : 11201,
    'favorite_dish' : 'stuffed peppers',
    'url' : 'http://www.lillobrooklyn.com'
}


# TODO: Print each dictionary
print(f"A few restaurants you may want to visit if you are in New York are:\
\n\n{nyc_restaurant_1['name']}\naddress: {nyc_restaurant_1['address']}\n{nyc_restaurant_1['city']}, {nyc_restaurant_1['state']} \
{nyc_restaurant_1['zip_code']}\nwebsite: {nyc_restaurant_1['url']}\nTry the {nyc_restaurant_1['favorite_dish']}!\
\n\n{nyc_restaurant_2['name']}\naddress: {nyc_restaurant_2['address']}\n{nyc_restaurant_2['city']}, {nyc_restaurant_2['state']} \
{nyc_restaurant_2['zip_code']}\nwebsite: {nyc_restaurant_2['url']}\nTry the {nyc_restaurant_2['favorite_dish']}!\
\n\n{nyc_restaurant_3['name']}\naddress: {nyc_restaurant_3['address']}\n{nyc_restaurant_3['city']}, {nyc_restaurant_3['state']} \
{nyc_restaurant_3['zip_code']}\nwebsite: {nyc_restaurant_3['url']}\nTry the {nyc_restaurant_3['favorite_dish']}!\
\n\n")

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''

print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
nyc_restaurant_1.pop('favorite_dish')
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
print(nyc_restaurant_1)

print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
nyc_restaurant_2['address'] = '211 52nd St.'
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
print(f"address: {nyc_restaurant_2['address']}\n{nyc_restaurant_2['city']}, {nyc_restaurant_2['state']} \
{nyc_restaurant_2['zip_code']}")
# TODO: Print the updated dictionary.
print(nyc_restaurant_2)

print()