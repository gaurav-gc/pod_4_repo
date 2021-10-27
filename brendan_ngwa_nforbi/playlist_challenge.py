# Music playlist challenge!
# In this challenge, you'll have to both work on this script, and the accompanying script playlist_functions.py
# All of your functions should be in the other script (playlist_functions.py)
# But, you'll run your functions here

# 1 Import all the functions in playlist_functions.py
from playlist_functions import *
#import numpy as np
# This code initializes your playlist as an empty list. no songs in it yet!
my_playlist = []
print(len(my_playlist))

# 2 Check what is in your playlist using the display_playlist() function
# HINT: the display_playlist() function in playlist_functions.py to figure out how to use it
print('Question 2')
display_playlist(my_playlist)

# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)
add_song(my_playlist, {'artist': 'Frank Ocean', 'title': 'Pyramids'})
print(my_playlist)

'''
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
'''
display_playlist(my_playlist)

# 4 Check that you've added the song by running the display_playlist() function again
print('Question 4')
display_playlist(my_playlist)
print(type(range(len(my_playlist))))
print((range(len(my_playlist))))
# 5 Add 2 more songs to my_playlist, then display it again using the display_playlist() function
print('Question 5')
add_song(my_playlist, {
    'artist': 'Flamagra', 'title': 'More'
})
add_song(my_playlist, {
    'artist': 'Kaytranada', 'title': 'No Vex Oh'
})



# 6 In playlist_functions.py, define a function called get_playlist_length()
# See playlist_functions.py for details on how to define this function
# THEN, call that function in this script to get the length of my_playlist
print('Question 6')
num_of_tracks = get_playlist_length(my_playlist)
print(f'Your playlist has {num_of_tracks} songs')

# 7 At the top of this script, import numpy using the usual alias

# 8: Using numpy, calculate the average monthly plays for a song
# TODO: using the mean() function from numpy, calculate the average of monthly_plays
# You don't have to write any functions for this question
print('Question 8')
monthly_plays = [127030, 274920, 232453, 98278, 500301, 235462]
#print(round(np.mean(monthly_plays), 2))

# BONUS In playlist_functions.py, define a new function called play_track()
# See playlist_functions.py for details on how to define this function
# Then play a few tracks, and run display_playlist() again to make sure it works
print('BONUS')

def play_track(playlist, track=1):
    print(f'Now playing track {track}, {playlist[track-1]["title"]} by {playlist[track-1]["artist"]}')

def play_track(playlist, track=1):
    track_index = track-1
    print(f'Now playing track {track}, {playlist[track-1]["title"]} by {playlist[track-1]["artist"]}')
