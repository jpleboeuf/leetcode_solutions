CREATE TABLE IF NOT EXISTS Sales (sale_id INT, product_id INT, year INT, quantity INT, price INT);
-- Table should have been named `Products`...
CREATE TABLE IF NOT EXISTS Product (product_id INT, product_name VARCHAR(10));
TRUNCATE TABLE Sales;
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
  ROW(1, 100, 2008, 10, 5000),
  ROW(2, 100, 2009, 12, 5000),
  ROW(7, 200, 2011, 15, 9000);
TRUNCATE TABLE Product;
INSERT INTO Product (product_id, product_name) VALUES
  ROW(100, 'Nokia'),
  ROW(200, 'Apple'),
  ROW(300, 'Samsung');
