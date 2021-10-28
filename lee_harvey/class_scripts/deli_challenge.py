print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
# Check that the meat chosen is offered

meats = [meat.capitalize() for meat in meats]
cheeses = [cheese.capitalize() for cheese in cheeses]

def check_meat(m):
    if m in meats:
        return 1
    return 0
# Check that the cheese chosen is offered
def check_cheese(c):
    if c in cheeses:
        return 1
    return 0
# Procure meat choice & verify
def get_meat():
    x = 1
    while x:
        m = input(f"Please choose the meat from the following choices: \n{str.join(', ', meats)}\n").capitalize()
        if check_meat(m): 
            x = 0
            return m
# Procure cheese choice & verify
def get_cheese():
    x = 1
    while x:
        c = input(f"Please choose the cheese from the following choices: \n{str.join(', ', cheeses)}\n").capitalize()
        if check_cheese(c): 
            x = 0
            return c
# Check the validity of the choice
def check_sandwich(s):
    if s in sandwiches:
        return 1
    return 0

def order(s):
    s = str.join(' & ', s)
    if s in menu:
        return s


#print(meats, cheeses)

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for meat in meats:
    for cheese in cheeses:
        sandwiches.append([meat, cheese])
# print(sandwiches)
menu = [str.join(' & ', sammy) for sammy in sandwiches]
print(str.join("\n", menu))
print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
meat_choice = get_meat()
cheese_choice = get_cheese()
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
if check_sandwich([meat_choice, cheese_choice]):
    sandwich = order([meat_choice, cheese_choice])
    print(f"Great choice! 1 {sandwich} coming right up!")
else:
    print("I'm sorry, that choice is not yet available. Please check back to see if it has been added!")