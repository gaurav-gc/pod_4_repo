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
clients_name = input("Type clients name here. ")
# TODO: Write code to ask the client his savings and save it to another variable.
clients_saving = int(input("type clients savings here. "))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.

stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
#stock/clients_saving 
if stock == "amzn":
    # Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
    print(f"{clients_name} has {clients_saving} in savings and he can buy {int(clients_saving/amazon)} shares of amazon at the current price of {amazon}. ")
elif stock =="aapl":
    print(f"{clients_name} has {clients_saving} in savings and he can buy {int(clients_saving/apple)} shares of apple at the current price of {apple}. ")
elif stock =="fb":
    print(f"{clients_name} has {clients_saving} in savings and he can buy {int(clients_saving/fb)} shares of facebook at the current price of {fb}. ")
elif stock =="goog":
    print(f"{clients_name} has {clients_saving} in savings and he can buy {int(clients_saving/google)} shares of google at the current price of {google}. ")
elif stock =="msft":
    print(f"{clients_name} has {clients_saving} in savings and he can buy {int(clients_saving/msft)} shares of microsoft at the current price of {msft}. ")    
else :
    print(" There are no stocks here")

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

print()