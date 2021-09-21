print("\nChallenge 3.1: Debug code snippets")
#Debug each snippet in order

print()

print("Code Snippet 1:")

u = 5
v = 2
# Added another = sign
if u * v == 10:
    print(f"The product of u ({u}) and v ({v}) is 10")
else:
    print(f"The product of u ({u}) and v ({v}) is not 10")

print()

print("Code Snippet 2:")
x = 15
y = 25
z = 30

# Added colons after elif and else
if z < x:
    print("z is less than x")
elif z > x and z < y:
    print("z is between x and y")
else:
    print("z is greater than y")

print()

print("Code Snippet 3:")

#modify the comparison operator below so the assert statement passes
#update the print statement to reflect changes to the code

a = 1
b = 1
c = (a == b)

print(f"The value of c ({c}) is True since a ({a}) is equal to b ({b}). \
\nChanged the comparison operator to equals to ensure true evaluation.")
assert(c == True) #Do not change this line

print()

print("Code Snippet 4:")

#modify exactly one boolean operator in the assignment of d, so that d evaluates to False
# Changed the first comparison operator to evaluate to false
d = (5 > 7) or not (8 < 20)
# TO DO: Explain how d is set to False in a print statement
assert(d == False) #Do not change this line
print("Since 'or' requires both to be false in order for 'd' to stay false, \nI modified \
the first comparison operator to greater than instead of less than.")

print()

print("Code Snippet 5:")

#modify the comparison operator so o evalutes to true
#update the print statement to reflect the changes

m = "GOAT"
n = "goat"

o = (m != n)

print (f"The value of o ({o}) is True since Python is case-sensitive. \
\nModified the equal comparitor to the not equal comparitor.")
assert(o == True) #Do not change this line

print()
print("CHALLENGE COMPLETE!\n")