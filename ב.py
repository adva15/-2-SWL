import sqlite3

# connector
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Reception:
input_name = input("Name or part of a movie Name [brings back all the movies]: ")

cursor.execute("SELECT movie_name FROM movies WHERE movie_name LIKE ?", ('%' + input_name + '%',))
movies = cursor.fetchall()

# Query Checking:
if movies:
    for movie in movies:
        print(f"movie name: {movie[0]}")
else:
    print(f"There is no movie with such a name '{input_name}' ")

# write the data into the db file
conn.commit()

# close connection
conn.close()
