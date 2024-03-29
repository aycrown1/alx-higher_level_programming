-- Import the temperature data from the SQL
source temperatures.sql;

-- Display the top 3 city temperatures during July and August
SELECT city, AVG(value) AS temperature
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY temperature DESC
LIMIT 3;
