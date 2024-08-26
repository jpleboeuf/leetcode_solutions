CREATE TABLE IF NOT EXISTS Products (product_id INT, low_fats ENUM('Y', 'N'), recyclable ENUM('Y','N'));
TRUNCATE TABLE Products;
INSERT INTO Products (product_id, low_fats, recyclable) VALUES ('0', 'Y', 'N');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES ('1', 'Y', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES ('2', 'N', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES ('3', 'Y', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES ('4', 'N', 'N');

# Write your MySQL query statement below
DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (
  SELECT p.product_id
  FROM Products p
  WHERE p.low_fats = 'Y' AND p.recyclable = 'Y'
);
SELECT * FROM Solution;

# Example 1:
CREATE TABLE IF NOT EXISTS Example1 (product_id INT);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (product_id) VALUES (1);
INSERT INTO Example1 (product_id) VALUES (3);
# Test against Example 1:
CHECKSUM TABLE Example1, Solution;
