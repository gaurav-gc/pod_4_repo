'''
For this challenge, you will work in groups of 2 to 'pair program'
You'll need to work together to complete this challenge!
In general, 1 person should be typing, and the other should be leading what to code
But, it is always okay to swap roles or for the typing person to add their ideas too

-------------------------------------------------------------------


Your challenge: Make a bank account!
In this challenge, we want to make a bank account with 3 crucial functions
-create_account() - this function will initialize a bank account
-deposit() - add money to the account
-withdraw() - remove money from the account


PART 1: create_account()
This function should make a bank account!
The function does not need to take any arguments
The function should prompt the user using input() for username/password
The function should return a dictionary with 3 key/value pairs:
-username (string, should be what the user inputs)
-password (string, should be what the user inputs)
-balance (float, initialize this to 0)
'''
from getpass import getpass
from random import seed, random

print('PART 1\n')
# TODO: define the create_account() function here and make sure it works
# HINT: make sure it works by doing something like my_account = create_account()
# Then print out my_account to see whether it has the correct info
my_account = []
seed(100000)
def create_account():
    account = {}
    account['username'] = input("User Name: ")
    account['password'] = getpass(prompt='Password: ')
    account['acct_num'] = int(random() * 100000000)
    account['balance'] = 0.0
    return account

def display_account(acct):
    for key in acct:
        print(f"{key}: {acct[key]}")

print()
my_account = create_account()
display_account(my_account)

'''
PART 2: deposit()
This function should make a deposit to add money to the account
The function should take 2 arguments
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to deposit)

The function does not need to return anything, but should increase the balance value by the appropriate amount

Test your function by making a few deposits to your account, then printing out your account
'''

print('PART 2\n')
# TODO define the deposit() function here and make sure it works
def deposit(acct, amt):
    acct['balance'] += amt

deposit(my_account, 300)
display_account(my_account)
deposit(my_account, 3150)
display_account(my_account)


'''
PART 3: withdraw()
This function should make a withdrawal to take money out of the account
The function should take 2 arguments:
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to withdraw)

FIRST, the function should check whether there is enough money in the account to withdraw the requested amount
-If there is enough money, the function should decrease the balance value by the appropriate amount
-If there is not enough money, the function should print a message about the balance and tell the user there is not enough available to make that withdrawal

Test your function by making several withdrawals to your account
-try some you think will work AND some you think will not be allowed (more than the balance)
'''

print('PART 3\n')
# TODO define the withdraw() function here and make sure it works
def withdraw(acct, amt):
    if acct['balance'] - amt > 0:
        acct['balance'] -= amt
    else:
        print(f"Account {acct['username']} does not currently have enough to cover the withdraw of ${amt:,.2f}.")

display_account(my_account)
withdraw(my_account, 3500)
withdraw(my_account, 150.37)
display_account(my_account)

'''
BONUS QUESTION 4: Password-protect withdrawal and deposits
Make new deposit_secure() and withdraw_secure() functions that prompt the user for their username/password FIRST
Only let the transaction proceed if they enter the right info!
Otherwise, tell the user the info is wrong

Test out your new functions to make sure they accept correct info, and let the user know if the password/username is incorrect
'''


# TODO: define password-protected withdraw_secure() and deposit_secure() functions
# HINT: there are tons of ways to do this correctly
# HINT: you can write any additional functions if you like

def deposit_secure(acct, amt):
    cnt = 3
    user = passwd = ''
    while cnt > 0:
        print('Deposit Access:\n')
        user = input('\tUser Name: ')
        passwd = getpass(prompt='\tPassword: ')
        if user == acct['username'] and passwd == acct['password']:
            acct['balance'] += amt
            print(f"The amount of {amt} has been added to your account.")
        else:
            print(f"The information you entered does not match what we have on file.\n\tYou have {cnt} chances left.")
            cnt -= 1
    if passwd != acct['password']:
        print("You are not authorized to access this account!")

def withdraw_secure(acct, amt):
    cnt = 3
    user = passwd = ''
    while cnt > 0:
        print('Withdraw Access:\n')
        user = input('\tUser Name: ')
        passwd = getpass(prompt='\tPassword: ')
        if user == acct['username'] and passwd == acct['password']:
            acct['balance'] -= amt
            print(f"The amount of {amt} has been deducted from your account.")
        else:
            print(f"The information you entered does not match what we have on file.\n\tYou have {cnt} chances left.")
            cnt -= 1
    if passwd != acct['password']:
        print("You are not authorized to access this account!")

display_account(my_account)
deposit_secure(my_account, 10526)
withdraw_secure(my_account, 4920)
display_account(my_account)