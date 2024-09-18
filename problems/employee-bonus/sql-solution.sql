DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b USING(empId)
WHERE IFNULL(b.bonus, 0) < 1000

);
