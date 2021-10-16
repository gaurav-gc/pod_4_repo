# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.
amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

stocks = {
    'amzn' : ['Amazon', amazon],
    'appl' : ['Apple', apple],
    'fb' : ['Facebook', fb],
    'goog' : ['Google', google],
    'msft' : ['Microsoft', msft]
}

stock_amt = 0
stock_details = []
u_name = ""
u_stock = ""

def get_stock():
    return input("\nWhich stock are you interested in? \
    \nType 'amzn' for Amazon, 'appl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. \n")

def get_name():
    return input("\nPlease enter your name: ")

def get_savings():
    return int(input("\nPlease enter the amount of savings you would like to work with: "))

def evaluate(s):
    for stock in stocks:
        if s == stock: return stocks[stock]
    evaluate(get_stock())

def stock_purchase(sa, us):
    if sa and us:
        if int(us / sa):
            return 0
    return 1

def report(name, savings, stock, cost):
    print(f"{name} has {savings} in savings and he can buy {int(savings / int(cost))} of {stock} at the current price of {cost}.\n")

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Taking user input")
# Write code to ask the client his name and save it to a variable..
u_name = get_name()
# Write code to ask the client his savings and save it to another variable.
u_savings = get_savings()

if u_savings < apple:
    print(f"You do not have enough money to invest.  Sorry {u_name}.\n")
    exit()
# Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
u_stock = get_stock()

print()

print("Challenge 3.2.2: Perform user-specific calculations")
# You have all 3 user inputs stores in variables. 
# Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
# assert(u_stock == 'amzn' or u_stock == 'appl' or u_stock == 'fb' or u_stock == 'goog' or u_stock == 'msft')
# assert(u_savings > 0)

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

# More concise way

stock_details = evaluate(u_stock)
stock_amt = stock_details[1]
while stock_purchase(stock_amt, u_savings):
    print(f"\nI'm sorry, {u_name}, you don't have enough to purchase the {stock_details[0]} stock.  Please choose another.\n")
    stock_details = evaluate(get_stock())
    stock_amt = stock_details[1]

print()

print("Challenge 3.2.3: Output for the user the result")
# Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
report(u_name, u_savings, stock_details[0], stock_amt)

print()