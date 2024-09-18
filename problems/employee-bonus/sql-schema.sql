-- Table should have been named `Employees`...
CREATE TABLE IF NOT EXISTS Employee (empId INT, name VARCHAR(255), supervisor INT, salary INT);
-- Table should have been named `Bonuses`...
CREATE TABLE IF NOT EXISTS Bonus (empId INT, bonus INT);
TRUNCATE TABLE Employee;
INSERT INTO Employee (empId, name, supervisor, salary) VALUES
  ROW(3, 'Brad',   NULL, 4000),
  ROW(1, 'John',   3,    1000),
  ROW(2, 'Dan',    3,    2000),
  ROW(4, 'Thomas', 3,    4000);
TRUNCATE TABLE Bonus;
INSERT INTO Bonus (empId, bonus) VALUES
  ROW(2,  500),
  ROW(4, 2000);
