
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()

count = 0

for food in meats:
    meats[count] = food.capitalize()
    count = count + 1
print(meats)
print()

count = 0

for food in cheeses:
    cheeses[count] = food.capitalize()
    count = count + 1
print(cheeses)
print()


print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []

for carne in meats:
    for queso in cheeses:
        combo = carne + ' & ' + queso
        sandwiches.append(combo)

print(sandwiches)
print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
order = input('What type of sandwich would you like: ')
# TODO: Loop over the sandwiches list.
for option in sandwiches:        
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'    
    if order == option:
        print(f'Great choice! 1 {option} coming right up!')