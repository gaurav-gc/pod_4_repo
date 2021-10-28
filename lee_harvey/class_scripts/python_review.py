# The following code is a review of all material covered up to and including OOP.
# The code is spaced for easy readability.

# Imports for numpy and the companion python_review_classes_&_functions.py.

import numpy as np

from python_review_classes_and_functions import *

# The print() statement, or function, is used to display information in the terminal.
# Not only is it used to give users of the software feedback, it can also be used by developers for debugging.
# By itself it provides blank lines in the terminal.
print()


# Variables can be called anything.  It is usually named to help with the understanding and readability of the code.
# The name is dependant on the developer to choose and make the code understandable by other developers.
# Users of the software never see the variables, only the values they contain that you choose to show them.

# A variable decloration, which can have any name, defined in snake-case with an assignment of an integer.

number = 0  # It is read, variable number assigned zero.

print('Line 25: variable number')
print(number)
print()

# A variable declaration defined as a float.
dotted_number = 3.37

print('Line 32: variable dotted_number')
print(dotted_number)
print()

# Boolean variable declaration assigning false.
is_true = False

print('Line 39: variable is_true')
print(is_true)
print()

# A variable declaration defined as a string using single quotes.
single_quotes = 'This is a string.'

# A variable declaration defined as string using double quotes.
double_quotes = "This is a string."

fstring = f'This is an f-string that can have formatting.\tWith many different possibilities.\n'

# When displayed, the difference between the two variables is lost.  The user of the software will not know the difference.
# Developers will see and know the difference though.  Whichever you use, be consistent.

print('Line 52 & 54: variables single_quotes and double_qotes')
print(single_quotes)
print()
print(double_quotes)
print()
print(fstring)


print('Lists:\n')
# A list is a vdata-type in python.  Values are indexed by numbers starting with 0. An empty declaration.
cars = []

# Use the type() function to return what data-type a variable is.
print(type(cars))

# Display the empty list in the terminal.
print(cars)
print()

# Reassigning the cars list with a few classics
cars = ['Mustang', 'Chevelle', 'Corvette', 'Camero', 'Mustang']

print('Result of cars assignment on line 73')
print(cars)
print()

# Showing the number of items in a list using the len() function.
items_in_cars_list = len(cars)

print('Line 80: len() result')
print(items_in_cars_list)
print()

# You could also use the count() method to access how many times an item is present
mustangs_in_cars_list = cars.count('Mustang')

print('Line 87: The result of cars.count(\'Mustang\').')
print(mustangs_in_cars_list)
print()

# To many mustangs, use the pop() method to remove the last one and assign it to the ford variable.  
ford = cars.pop()

print('Line 94: The result of the cars.pop() method.')
print(cars)
print()

# The pop() method can also take a number argument to access the value at that index.  
# Assigning the chevy variable with Chevelle, which is at index 1 (second item in the list).
chevy = cars.pop(1)

print('Line 102: The result of the cars.pop(1) method.')
print(cars)
print()

cars.append('Chevelle')
# Use the remove() method to delete a specific value.
cars.remove('Mustang')

print('Line 109: The result of the cars.remove(\'Mustang\') method.')
print(cars)
print()

# Creating a new list with Dodge classics.
dodge = ['Challenger', 'Charger']

print(dodge)
print()

# Adding the Mustang back to the list using append().
cars.append(ford)

print(cars)
print()

# Adding the dodge list to the cars list using extend().
cars.extend(dodge)

print(cars)
print()
# If you had used append() instead of extend() to add the dodge in the last index of cars would be another list containg Challenger and Charger.

print('Dictionaries:\n')

# Create a dictionary, accounts, with the key username value of Bob and the key password with the value *******
accounts = {
    'username' : 'Bob',
    'password' : '*******'
}

print(accounts)
print()
# Creating a new key in the acconts dictionary with the key access time and the value 13:45:23 (hours:minutes:seconds in military time).
accounts['access time'] = '13:45:23'

print(accounts)
print()

# Assign keys a list of all the keys in the accounts dictionary with the keys() method.
keys = accounts.keys()

print(accounts)
print(keys)
print()

# Assign values with a list of the values in the accounts dictionary with the values() method.
values = accounts.values()

print(accounts)
print(values)
print()

# Remove the access time item in accounts dictionary using the pop() method.
accounts.pop('access time')

print(accounts)
print()

# Completely clear a dictionary with the clear() method.
accounts.clear()

print(accounts)
print()

print('Nested Data:\n')
# Declaration of vehicles list.
vehicles = []


print(type(vehicles))
print()

# Using a for loop to populate the dictionary from the list cars.
for car in cars:
    # If the value of car is equivalent to Mustang
    if car == 'Mustang':
        
        # Create the dictionary with the key make and assign it Ford, and the key model and assign it car then append the dictionary to the list.
        vehicles.append({'make' : 'Ford', 'model' : car})
    
    # If the letters Ch are in the car variable and car is not equivalent to Chevelle.
    elif 'Ch' in car and car != 'Chevelle':
        
        # Create the dictionary with the key make and assign it Dodge, and the key model and assign it car then append the dictionary to the list.
        vehicles.append({'make' : 'Dodge', 'model' : car})
    else:
        # Create the dictionary with the key make and assign it Chevy, and the key model and assign it car then append the dictionary to the list.
        vehicles.append({'make' : 'Chevy', 'model' : car})

print(vehicles)
print()

# From the python_review_classes_and_functions.py file.
print('Printing vehicles using the print_nested() function.')
print_nested(vehicles)
print()

print('OOP:\n')
print()

# The class is defined in the companion file python_review_classes_&_functions.py.
account = Accounts('bob')
print()

# Print to the terminal what is in account.
account.display()

# Set the password attribute.
print(f'Set the password for {account.username}')
account.set_password()
print()
print()

# Use the change_owner method
print('The change_owner method:')
account.change_owner()
print()
print()

# Define an instance of the Administrator class in the variable admin, making it an object of Administrator().
admin = Administrator('mike')

# Use the parent (super) class to set the password.
print(f'Set the password for {admin.username}')
admin.set_password()
print()
print()

# Show the account in the terminal.
admin.display()
print()
print()

# Use the change_owner() method
print('The change_owner method:')
admin.change_owner()
print()
print()

# Parent method to delet an account.
print(f"Deleting {account.username} from accounts:")
admin.delete_account(account)
print()
print()
# The results of the account deletion.
account.display()
print()
print()
# Another look at the admin object.
admin.display()
print()
print()
print()
print()
# There is another function in the companion fiile.  Find the name and call it on line 254 (hint, it does not begin with _).
