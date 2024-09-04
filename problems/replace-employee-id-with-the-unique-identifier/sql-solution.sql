DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT i.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI i ON i.id = e.id

);
