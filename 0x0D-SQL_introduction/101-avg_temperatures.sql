-- Import the temperature data from the SQL
source temperatures.sql;

-- Calculate the average temperature in Fahrenheit for each city and order by temperature descending
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
