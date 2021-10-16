# Music playlist challenge!
# In this challenge, you'll have to both work on this script, and the accompanying script playlist_functions.py
# All of your functions should be in the other script (playlist_functions.py)
# But, you'll run your functions here

# 1 Import all the functions in playlist_functions.py
# imported all functions from playlist_functions using '*' as wildcard
from playlist_functions import *
# This code initializes your playlist as an empty list. no songs in it yet!
my_playlist = []


# 2 Check what is in your playlist using the display_playlist() function
# HINT: the display_playlist() function in playlist_functions.py to figure out how to use it
print('\nQuestion 2')
# call display_playlist function from playlist_function to display my_playlist
display_playlist(my_playlist)

# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)

'''
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
'''
# create a song dictionary
song1 = {'artist': 'Prince', 'title': '1999'}
# call add_song function from playlist_functions to add song dictionary to my_playlist
add_song(my_playlist, song1)

# 4 Check that you've added the song by running the display_playlist() function again
print('\nQuestion 4')
# call display_playlist functions from playlist_function to display my_playlist
display_playlist(my_playlist)

# 5 Add 2 more songs to my_playlist, then display it again using the display_playlist() function
print('\nQuestion 5')
# create a second song dictionary
song2 = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
# create a third song dictionary
song3 = {'artist': 'Pink Floyd', 'title': 'Hey You'}
# call add_song function from playlist_functions to add second song dictionary to my_playlist
add_song(my_playlist, song2)
# call add_song function from playlist_functions to add third song dictionary to my_playlist
add_song(my_playlist, song3)
# call display_playlist functions from playlist_function to display my_playlist
display_playlist(my_playlist)

# 6 In playlist_functions.py, define a function called get_playlist_length()
# See playlist_functions.py for details on how to define this function
# THEN, call that function in this script to get the length of my_playlist
print('\nQuestion 6')
# call get_playlist_length function from playlist_functions to return the length of my_playlist
print(get_playlist_length(my_playlist))

# 7 At the top of this script, import numpy using the usual alias
import numpy as np

# 8: Using numpy, calculate the average monthly plays for a song
# TODO: using the mean() function from numpy, calculate the average of monthly_plays
# You don't have to write any functions for this question
print('\nQuestion 8')
monthly_plays = [127030, 274920, 232453, 98278, 500301, 235462]
# call and numpy mean function to find the average of the values in the list montly_plays and print it
print(np.mean(monthly_plays))
# BONUS In playlist_functions.py, define a new function called play_track()
# See playlist_functions.py for details on how to define this function
# Then play a few tracks, and run display_playlist() again to make sure it works
print('\nBONUS')
# call play_track function from playlist_functions which prints a statement and add to a play count
play_track(my_playlist, 3)
play_track(my_playlist, 1)
play_track(my_playlist, 3)
play_track(my_playlist, 2)
play_track(my_playlist, 1)
play_track(my_playlist, 3)
play_track(my_playlist, 3)
print()
# call display_playlist functions from playlist_function to display my_playlist
display_playlist(my_playlist)
print()
