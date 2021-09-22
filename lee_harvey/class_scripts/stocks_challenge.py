print("Challenge 3.2: Playing with the stock market")

print()

def get_stock():
    return input("Which stock are you interested in? \
    \nType 'amzn' for Amazon, 'appl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. \n")

def get_name():
    return input("Please enter your name: ")

def get_savings():
    return int(input("Please enter the amount of savings you would like to work with: "))

def evaluate(s):
    # match s:  Requires Python 3.10 or higher
    #     case 'amzn':
    #         return amazon, 'Amazon'
    #     case 'appl':
    #         return apple, 'Apple'
    #     case 'fb':
    #         return fb, 'Facebook'
    #     case 'goog':
    #         return google, 'Google'
    #     case 'msft':
    #         return msft, 'Microsoft'
    if s == 'amzn':
        return amazon, 'Amazon'
    elif s == 'appl':
        return apple, 'Apple'
    elif s == 'fb':
        return fb, 'Facebook'
    elif s == 'goog':
        return google, 'Google'
    elif s == 'msft':
        return msft, 'Microsoft'
    else:
        s = get_stock()
def stock_purchase(sa, us):
    if int(us / sa):
        return 0
    else:
        return 1

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

stock_amt = 0
stock = 0
s_name = ''
u_name = ""
u_stock = ""

print("Challenge 3.2.1: Taking user input")
# Write code to ask the client his name and save it to a variable..
u_name = get_name()
# Write code to ask the client his savings and save it to another variable.
u_savings = get_savings()

if u_savings < apple:
    print(f"You do not have enough money to invest.  Sorry {u_name}.")
    exit()
# Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
u_stock = get_stock()

print()

print("Challenge 3.2.2: Perform user-specific calculations")
# You have all 3 user inputs stores in variables. 
# Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

assert(u_savings > 0)
#assert(u_stock == 'amzn' or u_stock == 'appl' or u_stock == 'fb' or u_stock == 'goog' or u_stock == 'msft')

# More concise way

stock, s_name = evaluate(u_stock)
while not stock:
    stock, s_name = evaluate(get_stock())

while stock_purchase(stock, u_savings):
    print(f"I'm sorry, {u_name}, you don't have enough to purchase that stock.  Please choose another.")
    stock, s_name = evaluate(get_stock())

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
print(f"{u_name} has {u_savings} in savings and he can buy {int(u_savings / stock)} of {s_name} at the current price of {stock}.")

print()

