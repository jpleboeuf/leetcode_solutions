CREATE TABLE IF NOT EXISTS Example1 (unique_id INT, name VARCHAR(20));
TRUNCATE TABLE Example1;
INSERT INTO Example1 (unique_id, name) VALUES
  ROW(NULL, 'Alice'),
  ROW(NULL, 'Bob'),
  ROW(2, 'Meir'),
  ROW(3, 'Winston'),
  ROW(1, 'Jonathan');
