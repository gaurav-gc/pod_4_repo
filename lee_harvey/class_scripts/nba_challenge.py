# Challenge 2.1
print('Challenge 2.1 & 2.2')
# Define murray's amount of 3 pointers
murray = 46
# Define vanvleet's amount of 3 pointers
vanvleet = 43
# Define harden's amount of 3 pointers
harden = 37

# Challenge 2.2
# Define murray's amount of 3 pointers
print(f"\nJamal Murray scored {murray} 3-point shots.")
# Display vanvleet in f-string
print(f"Fred VanVleet scored {vanvleet} 3-point shots.")
# Display harden in f-string
print(f"James Harden scored {harden} 3-point shots.\n")

# Challenge 2.3
print('Challenge 2.3 & 2.4')
# Define murray's 3 point attempts
murray_attempts = 93
# Define vanvleet's 3 point attempts
vanvleet_attempts = 110
# Define harden's 3 point attempts
harden_attempts = 109

# Challenge 2.4
# Display the attempt values for murray
print(f"The respective attempts for Murray are {murray_attempts} and shots made are {murray}.")
# Display the attempt values for vanvleet
print(f"The respective attempts for VanVleet are {vanvleet_attempts} and shots made are {vanvleet}.")
# Display the attempt values for harden
print(f"The respective attempts for Harden are {harden_attempts} and shots made are {harden}.\n")

# Challenge 2.5
print('Challenge 2.5')
# Define funtion to return percentage
def pointPercentage(m, a):
    return round(m / a * 100)

# Display the percentage for murray
print(f"Murray's 3 point shot percentage is {pointPercentage(murray, murray_attempts)}%.")
# Display the percentage for vanvleet
print(f"VanVleet's 3 point shot percentage is {pointPercentage(vanvleet, vanvleet_attempts)}%.")
# Display the percentage for harden
print(f"Harden's 3 point shot percentage is {pointPercentage(harden, harden_attempts)}%.\n\n")

# Challenge 3.1
print('Challenge 3.1')
# Display formatted paragraph, one sentence per line
print(f"The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\
\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\
\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\
\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\
\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\
\nThe Lakers ended the season atop the Western Conference with a record of 49-14.\
\nThey were narrowly behind the Bucks for the best record in the league.\
\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\
\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.\n")

# Challenge 3.2
print('Challenge 3.2')
about_lakers = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\
\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\
\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\
\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\
\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\
\nThe Lakers ended the season atop the Western Conference with a record of 49-14.\
\nThey were narrowly behind the Bucks for the best record in the league.\
\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\
\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.\n"

# Display this paragraph in upper case
print(about_lakers.upper())

# Challenge 3.3
print('Challenge 3.3')
# Define variable lakers_are_best
lakers_are_best = True
# Display challenge 3.3's answer
print(f"The Lakers are the best basketball team in the NBA, {lakers_are_best}, maybe.\n")

# Challenge 3.4
print('Challenge 3.4')
# Change data type of boolean to int
lakers_are_best = int(lakers_are_best)
# Display the lakers_are_best as an integer
print(f"The Lakers are the best basketball team in the NBA, {lakers_are_best}, maybe.")
print(f'{type(lakers_are_best)}')
# Change data type of lakers_are_best to string
lakers_are_best = str(bool(lakers_are_best))
print(f"The Lakers are the best basketball team in the NBA, {lakers_are_best}, maybe.")
print(f'{type(lakers_are_best)}')
print('Depending on if you convert the original or the integer version what you will get in the string.  Either True or 1 respectively.\n\n')

# Challenge 3.5
print('Challenge 3.5')
# Display the percentage for murray as a string
print(f"Murray's 3 point shot percentage is {str(pointPercentage(murray, murray_attempts))}% as a string.")
# Display the percentage for vanvleet as a string
print(f"VanVleet's 3 point shot percentage is {str(pointPercentage(vanvleet, vanvleet_attempts))}% as a string.")
# Display the percentage for harden as a string
print(f"Harden's 3 point shot percentage is {str(pointPercentage(harden, harden_attempts))}% as a string\n")
# Display what the difference is
print("The difference is that the percetages are now of the data type string.\n")

# Display the percentage for murray as an integer
print(f"Murray's 3 point shot percentage is {int(pointPercentage(murray, murray_attempts))}% as an integer.")
# Display the percentage for vanvleet as an integer
print(f"VanVleet's 3 point shot percentage is {int(pointPercentage(vanvleet, vanvleet_attempts))}% as an integer.")
# Display the percentage for harden as an integer
print(f"Harden's 3 point shot percentage is {int(pointPercentage(harden, harden_attempts))}% as an integer.\n")
# Display what the difference is
print("The difference is that the percetages are now of the data type integer.\n")

print('I do recognize that the original result of the equation for the average is a float.  My code format\'s this from \
the beginning, changing to an integer and providing a percentage sign for readibility.\n\n')