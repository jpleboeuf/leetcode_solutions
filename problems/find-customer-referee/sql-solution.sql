DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT c.name
FROM Customer c
WHERE NOT c.referee_id <=> 2

);
