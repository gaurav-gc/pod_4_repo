print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What is your name?")

# TODO: Write code to ask the client his savings and save it to another variable.
savings = int(input("Enter the amount in your savings account (as an integer)? "))

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'appl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
if stock == "amzn":
  totals = savings // amazon
  company = "Amazon"
  share_price = 3000
elif stock == "appl":
  totals = savings // apple
  company = "Apple"
  share_price = 100
elif stock == "fb":
  totals = savings // fb
  company = "Facebook"
  share_price = 250
elif stock == "goog":
  totals = savings // google
  company = "Google"
  share_price = 1400
elif stock == "msft":
  totals = savings // msft
  company = "Microsoft"
  share_price = 200
else:
  company = "unknown"  


print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
if company == "unknown":
  print(f'Sorry, {name}, {stock} is invalid')
else:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
    print(f'{name} has ${savings} in savings and can purchase {totals} of {company} at {share_price}')

print()

