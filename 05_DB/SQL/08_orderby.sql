SELECT * FROM users ORDER BY age ASC LIMIT 10;

SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

SELECT last_name, COUNT(*) as NumberofPeople FROM users GROUP BY last_name;