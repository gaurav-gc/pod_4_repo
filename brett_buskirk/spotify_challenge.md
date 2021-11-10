# Spotify Challenge #

## Question 1 ##

a) A better way of modeling the genre data would be to create a Genres table and linking the IDs of the differnt Genres in the Songs table instead of using just the value. See tables below for example.

b) This kind of relationship would be one-to-many

### Genres ###

| ID  | Genre     |
| --- | --------- |
| 1   | Rock      |
| 2   | Hip Hop   |

### Songs ###

| ID  | Song               | ArtistId | AlbumId | GenreId |
| --- | ------------------ | -------- | ------- | ------- |
| 1   | Here Comes the Sun | 1        | 1       | 1       |
| 2   | Come Together      | 1        | 1       | 1       |
| 3   | Let It Be          | 1        | 2       | 1       |
| 4   | Yesterday          | 1        | 3       | 1       |
| 5   | Hey Jude           | 1        | 4       | 1       |
| 6   | Hey JTC            | 2        | 5       | 2       |

## Question 2 ##

If we wanted to assign more than one genre to a song, we would need to create another table to represent both Songs and Genres:

### SongGenres ###

| ID  | GenreID | SongID |
| --- | ------- | ------ |
| 1   |    1    |    1   |
| 2   |    1    |    2   |
| 3   |    2    |    1   |