import sqlite3

# connector
conn = sqlite3.connect('movies.db')
conn.row_factory = sqlite3.Row

# cursor
cursor = conn.cursor()

##### read from db
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL UNIQUE, 
    genre TEXT NOT NULL,
    country TEXT NOT NULL,
    language TEXT NOT NULL,
    year INTEGER NOT NULL CHECK (year >= 2009), 
    revenue REAL NOT NULL CHECK (revenue >= 0)
)
''')

# all the INSERTS:
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Oppenheimer', 'Biography', 'USA', 'English', 2023, 960); """)
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Barbie', 'Comedy', 'USA', 'English', 2023, 1440);""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Dune Part Two', 'Sci-Fi', 'USA', 'English', 2024, 700);
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Everything Everywhere All at Once', 'Sci-Fi', 'USA', 'English', 2022, 140);
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('The Batman', 'Action', 'USA', 'English', 2022, 772);
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Spider Man No Way Home', 'Action', 'USA', 'English', 2021, 1920)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Top Gun Maverick', 'Action', 'USA', 'English', 2022, 1490)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('The Whale', 'Drama', 'USA', 'English', 2022, 55)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Guardians of the Galaxy Vol 3', 'Action', 'USA', 'English', 2023, 845)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Parasite', 'Thriller', 'South Korea', 'Korean', 2019, 266)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Train to Busan 2', 'Horror', 'South Korea', 'Korean', 2020, 92)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Decision to Leave', 'Mystery', 'South Korea', 'Korean', 2022, 23)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Joker', 'Drama', 'USA', 'English', 2019, 1074)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Tenet', 'Sci-Fi', 'USA', 'English', 2020, 365)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('The Irishman', 'Crime', 'USA', 'English', 2019, 8)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Ford v Ferrari', 'Drama', 'USA', 'English', 2019, 225)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('1917', 'War', 'UK', 'English', 2019, 385)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('The Farewell', 'Drama', 'USA', 'English/Chinese', 2019, 23)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('The Banshees of Inisherin', 'Comedy', 'Ireland', 'English', 2022, 49)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Django Unchained', 'Western', 'USA', 'English', 2012, 426)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Avengers Endgame', 'Action', 'USA', 'English', 2019, 2798)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Black Panther', 'Action', 'USA', 'English', 2018, 1347)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Coco', 'Animation', 'USA', 'English/Spanish', 2017, 807)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Mad Max Fury Road', 'Action', 'Australia', 'English', 2015, 380)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Inception', 'Sci-Fi', 'USA', 'English', 2010, 837)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('The Revenant', 'Adventure', 'USA', 'English', 2015, 532)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('La La Land', 'Musical', 'USA', 'English', 2016, 447)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('The Secret in Their Eyes', 'Crime', 'Argentina', 'Spanish', 2009, 34)
""")
cursor.execute("""
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('No Time to Die', 'Action', 'UK', 'English', 2021, 774);
""")


### א. Code showing all movies
cursor.execute("SELECT * FROM movies")
movies = cursor.fetchall()
for movie in movies:
  print(tuple(movie))

# write the data into the db file
conn.commit()

# close connection
conn.close()