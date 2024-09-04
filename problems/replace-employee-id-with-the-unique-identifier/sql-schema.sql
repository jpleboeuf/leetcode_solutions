CREATE TABLE IF NOT EXISTS Employees (id INT, name VARCHAR(20));
CREATE TABLE IF NOT EXISTS EmployeeUNI (id INT, unique_id INT);
TRUNCATE TABLE Employees;
INSERT INTO Employees (id, name) VALUES
  ROW(1, 'Alice'),
  ROW(7, 'Bob'),
  ROW(11, 'Meir'),
  ROW(90, 'Winston'),
  ROW(3, 'Jonathan');
TRUNCATE TABLE EmployeeUNI;
INSERT INTO EmployeeUNI (id, unique_id) VALUES
  ROW(3, 1),
  ROW(11, 2),
  ROW(90, 3);
