# Defined function to convert celsius to fahrenheit
def convert_to_fahrenheit(v):
    return (v - 32) * .5556 

# Defined function to convert fahrenheit to celsius
def convert_to_celsius(x):
    return x * 1.8 + 32

#  Provides the celsius of 100 degrees fahrenheit
celsius_100 = convert_to_fahrenheit(100)
# Provides the fahrenheit of 0 degrees celsius
celsius_0 = convert_to_celsius(0)
# Define variable degrees_c
degrees_c = 30.2
# Define variable degrees_f
degrees_f = 85.1

# 1. Display the 100 celsius conversion
print(str(celsius_100) + " fahrenheit")
# 1.a. Display type of resulting conversion
print(f'The result of the conversion is ' + type(convert_to_fahrenheit(celsius_100)) + '.\
\nBesides the type function, it will be a float do to the values in the equation.')

# 2. Display the 0 fahrenheit conversion
print(str(round(celsius_0))+ " celsius")

# 3. Display the 34.2 fahrenheit conversion
print(str(convert_to_celsius(34.2)) + " celsius")
# 4. Display the 5 celsius conversion
print(str(convert_to_fahrenheit(5)) + " fahrenheit\n")

# 5. Define the converted value of degrees_c for comparison
degrees_c_converted = convert_to_celsius(degrees_c)

# 5. Display the result of the comparison
if(degrees_c_converted == degrees_f):
    print("They are the same temperature")
elif(degrees_c_converted > degrees_f):
    print(f"{degrees_c} celsius is hotter.")
else:
    print(f"{degrees_f} fahrenheit is hotter.\n")