# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

print('Question 1')
employee_name = 'Ash Rahman'
print()

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name'
# create string variable and assign it the employee_name value after making it all lower case
lower_name = employee_name.lower()
# print employee name in lower case
print(lower_name)
print()
# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list'
# create list variable and assign it elements from the string employee_name split into a list of strings
names_list = lower_name.split(' ')
# print employee name as a list
print(names_list)
print()
# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names'
# creating a string variable and assigning it the elements of the list names_list joined by a '.' to create one string
joined_names = ".".join(names_list)
# print employee name joined by a '.'
print(joined_names)
print()
# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email'
# create a string variable and assign it the joined_name value after adding '@ripplemedia.com' to the end
email = joined_names + '@ripplemedia.com'
# print employee's new emaill address
print(email)
print()

print()

print('Question 2\n')

# Congratulations! Your team is expanding. Below is a list of their names:
names = ['Max Bartlett', 'Angelita Norris', 'Stewart Mueller', 'Dominique Henry', 'Carmela Gross', 'Bettie Mcmillan', 'Sara Ellison', 'Ira Anthony', 'Pauline Riley', 'Ben Weber',
         'Joanne Mcknight', 'Loren Gould', 'Jamar Singh', 'Amanda Vance', 'Tyrell Andrade', 'Jana Clements', 'Eddy Mcbride', 'Marsha Meyer', 'Elbert Shannon', 'Alyce Hull']
# create an empty list that new employee emails will be added to
emails = []

# We want to convert all their names into the same format from Question 1
# 2.1 TODO: Use a "for" loop to go over each name in the names list
for user_name in names:

# 2.2 TODO: Inside the "for" loop, create the email id by re-using the logic from Question 1 and...
=======
    # 2.2 TODO: Inside the "for" loop, create the email id by re-using the logic from Question 1 and...
    # create a string variable for the employee name after making it lower case
    lower_name = user_name.lower()
    # create a list variable for the emloyee name after splitting it into a list of strings
    names_list = lower_name.split(' ')
    # create a string variable for the value returned by joining the elements of name_list with a '.' to create one string
    joined_names = '.'.join(names_list)
    # create a variable created by joining '@ripplemedia.com' to the end of joined_name
    email = joined_names + '@ripplemedia.com'

# 2.3 TODO: ..add the email to the emails 
=======
# 2.3 TODO: ..add the email to the emails
    # add new employee email address to emails list
    emails.append(email)
# print the list of employee email addresses
print(emails)
print()
