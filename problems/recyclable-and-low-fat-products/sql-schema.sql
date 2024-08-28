CREATE TABLE IF NOT EXISTS Products (product_id INT, low_fats ENUM('Y', 'N'), recyclable ENUM('Y','N'));
TRUNCATE TABLE Products;
INSERT INTO Products (product_id, low_fats, recyclable) VALUES
  ROW('0', 'Y', 'N'),
  ROW('1', 'Y', 'Y'),
  ROW('2', 'N', 'Y'),
  ROW('3', 'Y', 'Y'),
  ROW('4', 'N', 'N');
