-- Table should have been named `Customers`...
CREATE TABLE IF NOT EXISTS Customer (id INT, name VARCHAR(25), referee_id INT);
TRUNCATE TABLE Customer;
INSERT INTO Customer (id, name, referee_id) VALUES
  ROW(1, 'Will', NULL),
  ROW(2, 'Jane', NULL),
  ROW(3, 'Alex', 2),
  ROW(4, 'Bill', NULL),
  ROW(5, 'Zack', 1),
  ROW(6, 'Mark', 2);
