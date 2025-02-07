import sqlite3

# connector
conn = sqlite3.connect('movies.db')
conn.row_factory = sqlite3.Row

# cursor
cursor = conn.cursor()

### Code showing all movies
cursor.execute("SELECT * FROM movies")
movies = cursor.fetchall()
for movie in movies:
  print(tuple(movie))

# write the data into the db file
conn.commit()

# close connection
conn.close()