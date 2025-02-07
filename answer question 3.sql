המשך חלק ב 

2. GROUP BY  שאילתות:
 ספור כמה סרטים יש מכל GENRE?.א.
SELECT movies.genre, COUNT(*) AS count_movies
FROM movies
GROUP BY genre;


 כמה רווח revenue ב. ?היה בכל שנה בתעשיית הסרטים
SELECT year, sum(revenue) AS sum_year_movies
FROM movies
GROUP BY year;


ג. ?מה ממוצע הרווחים לכל ז'אנר
SELECT genre, AVG(revenue) AS avg_revenue
FROM movies
GROUP BY genre;


ד. מה ממוצע הרווחים לכל ז'אנר עבור כל שפה בנפרד?
SELECT genre,language, AVG(revenue) AS avg_revenue
FROM movies
GROUP BY genre, language;


ה. ?באיזו שפה יש הכי פחות סרטים? רמז: מיין את הקבוצות בסדר עולה ובחר את הראשון
SELECT movies.language, COUNT(*) AS language_movie_less
FROM movies 
GROUP BY language 
ORDER BY language_movie_less ASC
LIMIT 1;

ו. ?לאיזו מדינה יש הכי הרבה סרטים? רמז: מיין את הקבוצות בסדר יורד ובחר את הראשון
SELECT movies.language, COUNT(*) AS language_movie_most
FROM movies 
GROUP BY language 
ORDER BY language_movie_most DESC
LIMIT 1;


ז. הצג את הז'אנרים בהם יש יותר מ- 2 סרטים
SELECT genre, COUNT(*) AS two_genre
FROM movies
GROUP BY genre
HAVING count(*) > 2;

 הצג שנים ) years ח. )בהם סך הרווחים היה גדול מ- 1,000 
SELECT year, SUM(revenue>1000) AS total_revenue
FROM movies
GROUP BY year 
HAVING SUM(revenue) > 1000
ORDER BY year;  
  

ט. הצג שפות בהן יש לפחות 3 סרטים
SELECT language,movie_name, COUNT(*) AS least_3_movies
FROM movies
GROUP BY language 
HAVING COUNT(*) >= 3




