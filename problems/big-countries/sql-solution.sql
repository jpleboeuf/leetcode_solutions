DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT c.name, c.population, c.area
FROM World c
WHERE c.area >= 3000000 OR c.population >= 25000000

);
