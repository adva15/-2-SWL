import sqlite3

# connector
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Reception:
movie_name = input("movie name:")
genre = input("genre:")
country = input("country:")
language = input("language:")
year = int(input("year:"))
revenue = int(input("revenue:"))

#
cursor.execute("""
    INSERT INTO movies (movie_name, genre, country, language, year, revenue)
    VALUES (?, ?, ?, ?, ?, ?)
""", (movie_name, genre, country, language, year, revenue))


conn.commit()

# Reception:
print(f"{movie_name} Added film To the movie table")

# # close connection
conn.close()
