# This is the companion class and function python file for the python_review.py in order to show imports multiple ways

# Defining a function that prints nested data.

# def keyword, indicates that we are defining a funtion.
# print_nested is the function name, like a variable, can be anything you can think of, but is recommended you choose something that pertains to it's purpose.
def print_nested(collection):
    # A for loop, item is the variable one level in collection.  If it is a list, the first iterstion, item will be 0.
    # Think of it like this: collection[item][sub_item]
    for item in collection:
        # Another for loop to access the nested data inside of collection, sub_item being another level in from item.
        for sub_item in item:
            print (f"{sub_item}: {item[sub_item]}")

# class reserved word defines the beginning of the template that will be used by this classes objects.  Accounts is the name of the class.
class Accounts():
    # def reserved word indicates a method for this class.  __init__ is the constructor template that must be defined for every class. 
    # The parameter self refers to the instance (item utilizing this class template) of the class, the object.
    # The parameter userid is needed to define the object, making the object unique in this class.  This is optional depending on the class you create.
    def __init__(self, userid):
        # username is a variable of this class.  It is a part of the object, tied to it, so is an attribute.  Like a key is to a dictionary.
        self.username = userid
        # password is an attribute.
        self.password = ''
        # permissions is an attribute containing a list
        self.permissions = ['read', 'write', 'execute']
    
    # This method takes self as a parameter, called display because of what it does.
    def display(self):
        # Shows the username and permissions in the terminal.
        print(f"User Name: {self.username}\nPermissions: {self.permissions}\n")
    
    # Another method of the Accounts() class.  This method defines the password attribute.
    def set_password(self):
        self.password = input('Please enter a password: ')
    
    # Another method of the Accounts() class.  This method verifies the password stored in self.password attribute.
    def get_password(self):
        # A counter variable set to 3 for the allowed number of iterations.
        times = 3
        # A boolean variable that indicates whether the passwords match.
        authenticated = False
        # A while loop the evaluates if times is greater than zero and not false (the default value of authenticated).
        while times > 0 and not authenticated:
            # Assign the input to value
            value = input('Password: ')
            # Evaluate value for equivalence to self.password value.
            if value == self.password:
                # Change the authenticated variables value to True
                authenticated = True
            else:
                # Decrease the counter by 1
                times -= 1
                # Let the user know it was wrong and they have a limited amount of times to get it right.
                print(f"Incorrect password.  You have {times} attempts left.")
        # Send the value of authenticated to the calling method
        return authenticated
    
    # A method that takes owvership of something.
    def change_owner(self):
        # Evaluate the password.
        if self.get_password():
            # If the permission to take ownership is in the list.
            if 'take ownership' in self.permissions:
                # Displays that the self.username has permission to take ownership.
                print(f"{self.username} is now the owner.")
            else:
                # Displays that the self.username does not have permission to take ownership.
                print(f"{self.username} does not have permission to change the owner.")
        else:
            # The password was wrong so we tell the user and exit this method.
            print('Try again at another time.')
    
    # A method to delete the account of obj (the account passed in).
    def delete_account(self, obj):
        if self.get_password():
            # If the permissions list contaings change settings.
            if 'change settings' in self.permissions:
                # Change the value of the attributes.
                obj.username = ''
                obj.password = ''
                # clear() is a list method to delete the contents of a list
                obj.permissions.clear()
            else:
                print(f"{self.username} does not have the permissions to remove an account.")
        else:
            print('Try again at another time.')

# A sub-class or child of the class Accounts()
class Administrator(Accounts):
    def __init__(self, handle):
        super().__init__(handle)
        self.permissions.extend(['change settings', 'take ownership'])

    def display(self):
        super().display()
        print('Warning: This account can make changes to the system.')












































































# Since the while loop is used repeatedly, and only two things changing is the message and the key (where the value will be stored), we can do this. Don;t call this by itself.  Internal function for calculate_tip() function.
def _get_input(item):
    # variable for the input
    value = 0
    # boolean for the while loop
    evaluation = True
    while evaluation:
        # get the input before the try block because there are two different conversions depending on the key passed in, aka item.
        value = input(f'Please enter the {item}: ')
        # attempt the conversion and catch any errors
        try:
            if item == 'pary':
                # The value is converted to an integer for the party key.
                value = int(value)
            else:
                # The value is converted to a float for the other keys (amount and tip).
                value = float(value)
        except:
            # If there is an error, we print the following then break out of the loop to ask again.
            print('Numbers only.')
            break
        # Getting the evaluation of value based on the key
        if item == 'tip':
            # Have to allow for a zero tip.  This evaluation will return true if value is less than 0 otherwise it will return false, 
            # assigning it to evaluation.
            evaluation = value < 0
        elif item == 'party':
            # Ther must be at least one person.  This evaluation will return true if value is less than 1 otherwise it will return false, 
            # assigning it to evaluation.
            evaluation = value < 1
        else:
            # The amount has to be greater than zero.  This evaluation will return true if value is less than or equal to  0 otherwise 
            # it will return false, assigning it to evaluation.
            evaluation = value <= 0
    # Sends the value from this function to the calling function, calculate_tip().
    return value












# A very simple tip calculator function
def calculate_tip():
    # Using the dictionary data type we can reduce the number of varables we are using.
    bill = {'amount' : 0,
    'tip' : 0,
    'party' : 0}
    # The necessary loop to ask for the correct input until it is received.
    # while loop with the evaluation of the amount, will repeat until the number is greater than zero.
    # while bill['amount'] <= 0:
    #     # This try block is necessary for catching any errors because something other than a number is entered.
    #     try:
    #         # Assigns the input to the amount key in the bill dictionary, converting the string from input to a float using the float() funtion.
    #         bill['amount'] = float(input('Please enter a dollar amount: $'))
    #     except:
    #         # If anything but a number is entered, print and loop, asking again.
    #         print('Numbers only.')
    
    # while bill['tip'] < 0:
    #     try:
    #         bill['tip'] = float(input('Please enter a percentage for the tip: %'))
    #     except:
    #         print('Numbers only.')
    
    # while bill['party'] < 1:
    #     try:
    #         bill['party'] = int(input('Please enter the number of people in your party: #'))
    #     except:
    #         print('Numbers only.')
    # There is a lot of repetition here.  So we should stop and refactor (rethink the process we used and implement a different way)
    
    # This list is necessary to accomplish the for loop to get input
    keys = bill.keys()
    # Using a for loop, reiterates until all values are recieved.
    for key in keys:
        bill[key] = _get_input(key)
    
    # The calculation of tip, tax and the total amout.
    bill['tip'] *= .01
    bill['tip amount'] = bill['tip'] * bill['amount']
    bill['tax amount'] = bill['amount'] * .10
    bill['total'] = bill['amount'] + bill['tax amount'] + bill['tip amount']
    # The calculation of the bill for each member of the party.
    bill['bill per person'] = bill['total'] / bill['party']
    
    # Print the values we are interested in.
    print(f"Tip: {bill['tip amount']:,.2f}")
    print(f"Total: {bill['total']:,.2f}")
    print(f"Per Person: {bill['bill per person']:,.2f}")