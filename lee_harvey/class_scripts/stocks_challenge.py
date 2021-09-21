print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# Write code to ask the client his name and save it to a variable..
u_name = input("Please enter you name: ")
# Write code to ask the client his savings and save it to another variable.
u_savings = int(input("Please enter the amount of savings you would like to work with: "))
# Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
u_stock = input("Which stock are you interested in? \
Type 'amzn' for Amazon, 'appl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
stock_amt = 0
stock = 0
s_name = ''
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. 
# Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

assert(u_savings > 0)
assert(u_stock == 'amzn' or u_stock == 'appl' or u_stock == 'fb' or u_stock == 'goog' or u_stock == 'msft')
if u_stock == 'amzn':
    stock = amazon
    s_name = 'Amazon'
elif u_stock == 'appl':
    stock = apple
    s_name = 'Apple'
elif u_stock == 'fb':
    stock = fb
    s_name = 'Facebook'
elif u_stock == 'goog':
    stock = google
    s_name = 'Google'
else:
    stock = msft
    s_name = 'Microsoft'


'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
print(f"{u_name} has {u_savings} in savings and he can buy {int(u_savings / stock)} of {s_name} at the current price of {stock}.")

print()

