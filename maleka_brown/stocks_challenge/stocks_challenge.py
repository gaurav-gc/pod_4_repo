from abc import ABCMeta


print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

# note for future ref: REVIST WITH G - Crt complex cond.
print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input('What is your name:')
print()
# TODO: Write code to ask the client his savings and save it to another variable.
saving = (int(input('Enter your savings amount:')))
#saving_1 = int(saving)

print(type(saving))


# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()


print("Challenge 3.2.2: Perform user-specific calculations")


def runCode(stock_name):
    print()
    print()
    print(f'{stock_name}')
    number_of_shares = saving/share_price
    print(number_of_shares)
    print()
    if saving > 100:
        ('can buy share')
        if stock == 'amzn':
            # print('amazon')
            runCode(amazon)
            share_price = amazon
            number_of_shares = saving/amazon
            # print(number_of_shares)
        elif stock == 'aapl':
            print('apple')
            share_price = apple
            number_of_shares = saving/apple
            print(number_of_shares)
        elif stock == 'fb':
            print('facebook')
            share_price = fb
            number_of_shares = saving/fb
            print(number_of_shares)
        elif stock == 'goog':
            print('google')
            share_price = google
            number_of_shares = saving/google
            print(number_of_shares)
        elif stock == 'msft':
            print('microsoft')
            share_price = msft
            number_of_shares = saving/msft
            print(number_of_shares)
    else:
        print('Need more money')

# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

# creating func


def runCode(stock_name):
    print()
    print()
    print(f'{stock_name}')
    number_of_shares = saving/share_price
    print(number_of_shares)
    print()


runCode(stock)
'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

# CODE:

print(f'{name} has {saving} in savings and he can buy {number_of_shares} of {stock} at the current price of ${share_price}')

print()
