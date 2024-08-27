CREATE TABLE IF NOT EXISTS Products (product_id INT, low_fats ENUM('Y', 'N'), recyclable ENUM('Y','N'));
TRUNCATE TABLE Products;
INSERT INTO Products (product_id, low_fats, recyclable) VALUES
  ROW('0', 'Y', 'N'),
  ROW('1', 'Y', 'Y'),
  ROW('2', 'N', 'Y'),
  ROW('3', 'Y', 'Y'),
  ROW('4', 'N', 'N');

# Example 1:
CREATE TABLE IF NOT EXISTS Example1 (product_id INT);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (product_id) VALUES
  ROW(1),
  ROW(3);
SELECT * FROM Example1;

# Solution:
DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (
  SELECT p.product_id
  FROM Products p
  WHERE p.low_fats = 'Y' AND p.recyclable = 'Y'
);
SELECT * FROM Solution;

# Test of Solution against Example 1:
CHECKSUM TABLE Example1, Solution;
