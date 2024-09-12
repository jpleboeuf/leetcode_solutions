CREATE TABLE IF NOT EXISTS Example1 (product_name VARCHAR(10), year INT, price INT);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (product_name, year, price) VALUES
  ROW('Nokia', 2008, 5000),
  ROW('Nokia', 2009, 5000),
  ROW('Apple', 2011, 9000);
