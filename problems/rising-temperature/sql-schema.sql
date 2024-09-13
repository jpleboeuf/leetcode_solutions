-- Table should have been named `Temperatures`...
CREATE TABLE IF NOT EXISTS Weather (id INT, recordDate DATE, temperature INT);
TRUNCATE TABLE Weather;
INSERT INTO Weather (id, recordDate, temperature) VALUES
  ROW(1, '2015-01-01', 10),
  ROW(2, '2015-01-02', 25),
  ROW(3, '2015-01-03', 20),
  ROW(4, '2015-01-04', 30);
