המשך חלק ב 

.3 שאילתות JOIN

 הצג את רשימת התיירים ביחד עם המדינות מהם הגיעו . רמז: JOIN INNER .א
SELECT tourists.first_name, tourists.last_name, countries.country_name AS from_countrie FROM tourists
INNER JOIN countries ON tourists.country_id = countries.id;


ב. הצג את רשימת התיירים ואת פרטי הטיול אליו הם משובצים , רק לתיירים משובצים
SELECT tourists.first_name, tourists.last_name, tours.tour_name, tours.description, tours.start_date ||', '|| tours.end_date AS Trip_details FROM tourists
INNER JOIN tours ON tourists.tour_id = tours.id
WHERE tourists.tour_id IS NOT NULL; 

יופיע NULL ג. בעמודות של פרטי הטיול הצג את רשימת כל התיירים ואת פרטי הטיול אליו הם משובצים , היכן שהתייר איננו משובץ 
SELECT tourists.*, tours.tour_name, tours.start_date, tours.end_date
FROM tourists
LEFT JOIN tours ON tourists.tour_id = tours.id;


ד. בשאילתא נפרדת, כתוב שאילתא המוחקת את אחד התיירים שלא נרשם לשום טיול .הצג את רשימת התיירים אשר אינם משובצים לשום טיול 
SELECT first_name, last_name, tour_id AS not_assigned_trip  FROM tourists 
WHERE tour_id IS NULL;

שאילתת מחיקה: 
DELETE FROM tourists
WHERE first_name = 'Leonardo' AND last_name = 'DiCaprio'


אחת קדימה. רמז: שאילתת UPDATE ו. בכדי שיהיה מספיק זמן להירשם, שנה את תאריך הטיולים )שאין להם בכלל נרשמים(, שנה הצג את רשימת הטיולים אשר אין שום תייר משובץ אליהם 
הצגת רשימת הטיולים אשר אין שום תייר משובץ אליהם:
SELECT tours.id, tours.tour_name, tours.start_date, tours.end_date, tour_id
FROM tours 
LEFT JOIN tourists ON tours.id = tourists.tour_id
WHERE tour_id IS NULL;

 שינוי תאריך הטיולים שאין להם בכלל נרשמים שנה אחת קדימה:
 UPDATE tours SET start_date = DATE(start_date, '+1 year'), end_date = DATE(end_date, '+1 year')
WHERE id IN ( SELECT tours.id FROM tours
LEFT JOIN tourists ON tours.id = tourists.tour_id
WHERE tour_id IS NULL);


ז. ספור לכמה טיולים אין שום תייר משובץ אפילו לא אחד
SELECT COUNT(*) AS tours_without_tourists
FROM tours 
LEFT JOIN tourists ON tours.id = tourists.tour_id
WHERE tour_id IS NULL;


ח. הצג את כל הצירופים האפשריים של כל התיירים מול כל הטיולים
SELECT tourists.first_name, tourists.last_name, tour_name
FROM tourists 
FULL JOIN tours;
