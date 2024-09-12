CREATE TABLE IF NOT EXISTS Visits(visit_id INT, customer_id INT);
CREATE TABLE IF NOT EXISTS Transactions(transaction_id INT, visit_id INT, amount INT);
TRUNCATE TABLE Visits;
INSERT INTO Visits (visit_id, customer_id) VALUES
  ROW(1, 23),
  ROW(2, 9),
  ROW(4, 30),
  ROW(5, 54),
  ROW(6, 96),
  ROW(7, 54),
  ROW(8, 54);
TRUNCATE TABLE Transactions;
INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES
  ROW(2, 5, 310),
  ROW(3, 5, 300),
  ROW(9, 5, 200),
  ROW(12, 1, 910),
  ROW(13, 2, 970);
