print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanfleet_3pts_made = 43
james_hardin_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanFleet made {fred_vanfleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_hardin_3pts_made} 3 point shots")
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_attempts_made = 93
fred_vanfleet_attempts_made = 110
james_hardin_attempts_made = 109
print()

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_attempts_made} 3 point shot attempts")
print(f"In the 2020 NBA playoffs, Fred VanFleet made {fred_vanfleet_3pts_made} 3 point shots and {fred_vanfleet_attempts_made} 3 point shot attempts")
print(f"In the 2020 NBA playoffs, James Harden made {james_hardin_3pts_made} 3 point shots and {james_hardin_attempts_made} 3 point shot attempts")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
jamal_murray_percent = jamal_murray_3pts_made / jamal_murray_attempts_made
fred_vanfleet_percent = fred_vanfleet_3pts_made / fred_vanfleet_attempts_made
james_hardin_percent = james_hardin_3pts_made / james_hardin_attempts_made
print(f"Jamal Murray's 3-point percentage was {jamal_murray_percent}")
print(f"Fred VanFleet's 3-point percentage was {fred_vanfleet_percent}")
print(f"James Harden's 3-point percentage was {james_hardin_percent}")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
giant_line_of_text = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\nThe Lakers ended the season atop the Western Conference with a record of 49-14.\nThey were narrowly behind the Bucks for the best record in the league.\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(giant_line_of_text)


print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print(giant_line_of_text.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_the_best = False
print(f"Do I think the Lakers are the best NBA team? {lakers_are_the_best}!")

print('Challenge 3.4: Type Conversion')
print(f"Integer: {int(lakers_are_the_best)}")
print(f"Float: {float(lakers_are_the_best)}")

print('Challenge 3.5: Type Conversion Part 2')
print(f"Jamal Murray's 3-point percentage string is {str(jamal_murray_percent)}")
print(f"Fred VanFleet's 3-point percentage string is {str(fred_vanfleet_percent)}")
print(f"James Harden's 3-point percentage string is {str(james_hardin_percent)}")
print(f"Jamal Murray's 3-point percentage integer is {int(jamal_murray_percent)}")
print(f"Fred VanFleet's 3-point percentage integer is {int(fred_vanfleet_percent)}")
print(f"James Harden's 3-point percentage integer is {int(james_hardin_percent)}")
