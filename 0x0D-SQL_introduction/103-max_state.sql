-- Your SQL script content

-- Import the temperature data from the SQL
source temperatures.sql;

-- Display the top 3 cities' temperatures during July and August
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
