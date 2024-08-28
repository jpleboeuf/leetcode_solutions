DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT p.product_id
FROM Products p
WHERE p.low_fats = 'Y' AND p.recyclable = 'Y'

);
