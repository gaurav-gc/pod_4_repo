######################################
######################################
############## Data Types ############
######################################
######################################
    # -	Booleans - True, False
    # - Integers - 1, 2, 3		
    #     Can be Positive, Negative and Zero	
    # - Floats - 1.0, 1.5, 10.38
    #     If you have a float in a mathematical equation, a float will always be returned
    # - Strings - “Hello 2 Students” “Cat” “What?”		 
    #     Escape Characters
    #         Line Break - \n
    #             -if you have a long string and want to break it up when it prints	
    #         Tab Indentation	- \t
    #             -each \t will create a tabbed line
    #     F Strings - variable = f'this is an {example} of an f string'
    #         -create strings using other variables
    #             EXAMPLE:
    #                 profit = 120
    #                 my_f_string = f‘The profit today is {profit}’
    #                 print(my_f_string)
                    
    #             ALSO- you can do math in the curlys
    #                 print(f ‘If i earn 200 and my expenses are 40, then my profit is $ {200 - 40}
    #     Concatenation - combine 2 strings together
    #         first - ‘diana’
    #         last = ‘rey’
    #         print (first + ‘’ + last)
    #     Upper and Lower Cases - .upper() // .lower()
    #         fullname = ‘Diana Rey’
    #         print(fullname.upper())
    #         print(fullname.lower())
######################################
######################################
##### Type Conversions Functions #####
######################################
######################################
    #  Type Conversion Functions - convert a value from one data type to another.
    
    # int(variable, object etc) - take a float or a string and turn it into an integer.	
        # NOTE: it does this not by rounding, but by truncating--it drops off all the numbers after the decimal. 
    # float(variable, object etc) - take an integer or a string and turn it into a float.
    # str(variable, object, etc) - take a float or an integer and turn it into a string. 
    # type(object) // type(name, bases, dict,variable) - will tell you its data type

######################################
######################################
############## Operators #############
######################################
######################################
    # are used to manipulate data. 	
        # =  equal	
        # + addition	
        # / division and always results in a float
        # - subtraction
        # * multiplication	
        # ** which performs exponentiation	
        # % which is the modulus (or remainder) operator	

    # Python will run the Operators according to PEMDAS
        # parentheses
        # exponents
        # multiplication
        # division
        # addition
        # subtraction
            

# Concatenation -  combining strings together. When we concatenate strings, we form a new string that is a collection of both strings' characters.

# input() - prints the string (in this case, it's called a prompt string) that we put in parentheses out to the shell so the user can read it.
#		number = int(input("Enter the starting number: "))
# 		end_number = number + 9
# 		while number <= end_number:
#  		   print(number)
# 	    number = number + 1

######################################
######################################
###### Conditional Statements ########
######################################
######################################
    # Statements that are only executed if the conditional expression is met.

    # IF/ELIF/ELSE code Blocks: 
    # 		if CONDITION no. 1:                         AKA : If this condition no 1. is True:
    #            code block no. 1                                   run code block no.1.
            # elif CONDITION no.2:                            elif condition no.1 is False, and condition no. 2 is True:
            #     code block no.2                                   run code block no.2
            # else:                                           else all the conditions listed above are False:
    #            code block no. 3                                   run code block no. 3

        # EXAMPLE:
    # 		if strawberry_stock > 0:
    # 		    print("I'm buying strawberry ice cream")
    # 		else:
    # 		    print("I'm buying chocolate ice cream")
    # OR
    # 		if strawberry_stock > 0:
    # 		    print("I'm buying strawbery ice cream")
    # 		elif chocolate_stock > 0:
    # 		    print("I'm buying chocolate ice cream")
    # 		else:
    # 	    print("I'm buying vanilla ice cream.”)

        # CONDITION is a Boolean expression - True or False
######################################
######################################
# COMBINING 2 CONDITION STATEMENTS
#     AND  - run this code block if BOTH of the statements are True
#         a = 200
#         b = 33
#         c = 500
#         if a > b and c > a:
#             print("Both conditions are True")

#     OR - run this code block if EITHER of these statements are True:
#         a = 200
#         b = 33
#         c = 500
#         if a > b or a > c:
#             print("At least one of the conditions is True")
#     NESTED IF STATEMENTS - if statements inside if statements
#         x = 41
#         if x > 10:
#             print("Above ten,")
#             if x > 20:
#                 print("and also above 20!")
#         else:
#             print("but not above 20.")
######################################
######################################
###### Comparison Operators ##########
######################################
######################################
 	# All 6 comparison operators and the condition under which each will return True:		
        #  x == y               # x is equal to y		
        #  x != y               # x is not equal to y		
        #  x > y                # x is greater than y		
        #  x < y                # x is less than y		
        #  x >= y               # x is greater than or equal to y		
        #  x <= y               # x is less than or equal to y

######################################
######################################
######## FOR / WHILE LOOPS ###########
######################################
######################################
# While Loop - keep looping while a condition is true
        # EXAMPLE: 
#       	while number <= 100 print(‘hello’)
#       	    -This would be an example of what is called indefinite iteration, 
#                meaning we don't know how many times we'll need to perform the loop body. 

# For Loop - allows us to repeat a task a specific number of times, and to use different data (such as a different name) each time we repeat.
#         EXAMPLE: 
#           	coworker_names = ["Mike", "Jessica", "Sheila", "Anton", "Kim"] 
#        		for name in coworker_names:     
#       	    print("Good morning, " + name + "!")

#           -The first line of the loop specifies a list of names.
#           -The code within the loop will execute once for each item in the list, with the value of the name 
#               variable being updated to have the value of each item in the list, in turn. 
#           -If there are 10 items in the list, the loops repeats 10 times.
#           -The variable name can be given any other name that we like.

# This is called definite iteration - have a definite (fixed, defined) number of times that we will perform the loop body.

######################################
######################################
############ MATHEMATICS #############
######################################
######################################
# Range - 
#   SYNTAX: range(start, stop, step)
        # start - what number to start
        # stop - what number to stop
        # step - how many numbers to increment by
            # EXAMPLE:
#1        		max_number = input("Print all positive even numbers less than:")
#2       		max_number = int(max_number)
#3 	        	for number in range(0, max_number, 2):
#4 	       	    print(number) 
                    # 1 we're asking user to input a number for us that will be our STOP NUMBER
                    # 2. we're saving that number to a variable and converting it into an integer
                    # 3. we're looping  through the number variable to find all the numbers from zero to the Max_number variable in increment
                    #     of 2.
                    # 4. We're printing each number within that range
######################################
######################################
# Rounding - 
    # SYNTAX : round(number, digits)
    #         number - the number you want rounded
    #         digits, how many decimal places you want it rounded to
         # EXAMPLE : 
            # x = round(5.76543, 3)
            # print(x)
######################################
######################################
# Average - 
# 		numbers = [2, 4, 6, 8]                  # list of numbers
# 		number_items = len(numbers)             # get number of items in the numbers variable
# 		sum_of_numbers = 0                      # set another variable to manipulate and add numbers to
# 		for number in numbers:                  # loop through the list adding up all the numbers
# 	     sum_of_numbers += number               # for each number found in NUMBERS variable, add it to sum_of_numbers
# 		 average = sum_of_numbers / number_items# get average

# len - gives us the number of items in a string, list, dictionary or any iterable data type
    # SYNTAX: len(object)

######################################
######################################
######### MANIPULATING DATA ##########
######################################
######################################
# SLICE
#     SYNTAX: slice(start, end, step)
#         start - Optional. An integer number specifying at which position to start the slicing. Default is 0
#         end	- An integer number specifying at which position to end the slicing
#         step - Optional. An integer number specifying the step of the slicing. Default is 1
        # EXAMPLE : 
        #     a = ("a", "b", "c", "d", "e", "f", "g", "h")      list of letters
        #     x = slice(3, 5)                                   Start the slice object at position 3, and slice to position 5
        #     print(a[x])                                       return the result
                                # returns: ('d', 'e')

# NOTE WITH INDEXES IN LISTS
#         When counting Indexes in lists, it ALWAYS start at ZERO
    #             a = ("a", "b", "c", "d", "e", "f", "g", "h")
    #  index number =   0    1    2    3    4    5    6    7

# When slicing, the END position will not be returned.  That is why the slice ends at 5.  If you wanted to include 5 in the return statement, change the END position to 6.

######################################
######################################
# INDEX LOOK UP
#     If you know the index number of the element you're trying to find, you can target it by  [index number] to the end of your list variable
#     EXAMPLE :
#         hello_world = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
#         print(hello_world[0])
#             returns: h

# To find the index number of an element use the index method:
    # SYNTAX: list.index(obj)
#     aList = [123, 'xyz', 'zara', 'abc']
#     print (aList.index('xyz'))
#                 Returns: 1
######################################
######################################
# REMOVE -  removes the specified item.
#     SYNTAX: list.remove("item to be removed")
#     EXAMPLE:
#         thislist = ["apple", "banana", "cherry"]
#         thislist.remove("banana")
#         print(thislist)
#                 RETURNS: thislist = ["apple", "cherry"]

# POP - removes the specified index.
#     SYNTAX: list.pop(1)
#         If you do not specify the index, the pop() method removes the last item.
#     EXAMPLE:
#         thislist = ["apple", "banana", "cherry"]
#         thislist.pop(1)
#         print(thislist)
#                 RETURNS: thislist = ["apple", "cherry"]
######################################
######################################
# SPLIT - splits a string into a list.
#     SYNTAX - string.split(separator, maxsplit)
#         separator - Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#         maxsplit - Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
                    # When maxsplit is specified, the list will contain the specified number of elements plus one.
#     EXAMPLE:
#         txt = "hello, my name is Peter, I am 26 years old"      text to be split
#         x = txt.split(",")                                     splitting the string by commas(,) and saving it to a variable
#         print(x)                                                returning the split results
#                         RETURN: ['hello', 'my name is Peter', 'I am 26 years old']
######################################
######################################
# APPEND - adds an element to the end of the list.
#     SYNTAX: list.append(elmnt)
#         elmnt - Required. An element of any type (string, number, object etc.)
#     EXAMPLE: 
#         fruits = ['apple', 'banana', 'cherry']
#         fruits.append("orange")
#             RETURNS: ['apple', 'banana', 'cherry', 'orange']
######################################
######################################
JOIN - takes all items in an iterable and joins them into one string.
    A string must be specified as the separator.
        SYNTAX: string.join(iterable)
            iterable - Required. Any iterable object where all the returned values are strings


######################################
######################################
############ DICTIONARY ##############
######################################
######################################
EXAMPLE: thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
######################################
######################################
 2 ways to access the items of a dictionary:
    -By referring to its key name, inside square brackets:
        x = thisdict["model"]
    -GET Method: 
        SYNTAX : x = thisdict.get("key")

######################################
######################################
Removing Items from dictionary

POP - removes the item with the specified key name:
    thisdict.pop("model")
    print(thisdict)

DEL - removes the item with the specified key name:
        del thisdict["model"]
        print(thisdict)
    can also delete the dictionary completely
        del thisdict
######################################
######################################
Update items from dictionary - 2 ways
    - Update method - 
        SYNTAX - thisdict.update({"key":value})
            EXAMPLE: Update the "year" of the car by using the update() method:
            thisdict.update({"year": 2020})
    - Change the value of a specific item by referring to its key name
            thisdict["year"] = 2018