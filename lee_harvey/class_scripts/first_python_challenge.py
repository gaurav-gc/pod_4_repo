print('1: Describe what is happening below by adding comments before each line')
# Assign box_1 'books'
box_1 = 'books'
# Assign box_2 'clothes'
box_2 = 'clothes'
# Assign box_3 'plants'
box_3 = 'plants'
# Assign box_4 'kitchen stuff'
box_4 = 'kitchen stuff'

# Print the four variables above
print('2: Print the variables box_1, box_2, box_3, box_4')
print(box_1, box_2, box_3, box_4, sep='\n')

# Define a variable address with a value
print('\n3.1: Declare a variable with the name "address", assign it any street name you like')
address = 'Last Chance Gulch'

# Print the previously defined variable address
print('\n3.2: Print the address variable')
print(address)

# Reassign box_2 and box_4 with other values and re-print the list of 
print('\n4: Reassign variables box_2 and box_4 with some other text and print box_1, box_2, box_3, box_4 again')
box_2, box_4 = 'new clothes', 'other stuff'
print(box_1, box_2, box_3, box_4, sep='\n')

# Fix the following line of code and uncomment
print('\n5.1: The line of code below is commented out because it produces many SyntaxErrors. Fix the problem and turn the comment back into regular Python code')
completion_message = 'Completed the first Python challenge!'
print(completion_message)

print('\n5.2: Turn the comment below back into regular Python code')
print(completion_message)
