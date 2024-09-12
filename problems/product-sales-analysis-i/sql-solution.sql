DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT p.product_name, s.year, s.price
FROM Sales s
LEFT JOIN Product p ON p.product_id = s.product_id

);
