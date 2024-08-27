CREATE TABLE IF NOT EXISTS Customer (id INT, name VARCHAR(25), referee_id INT);
TRUNCATE TABLE Customer;
INSERT INTO Customer (id, name, referee_id) VALUES
  ROW('1', 'Will', 'None'),
  ROW('2', 'Jane', 'None'),
  ROW('3', 'Alex', '2'),
  ROW('4', 'Bill', 'None'),
  ROW('5', 'Zack', '1'),
  ROW('6', 'Mark', '2');

# Write your MySQL query statement below
