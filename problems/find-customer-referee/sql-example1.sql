CREATE TABLE IF NOT EXISTS Example1 (name VARCHAR(25));
TRUNCATE TABLE Example1;
INSERT INTO Example1 (name) VALUES
  ROW('Will'),
  ROW('Jane'),
  ROW('Bill'),
  ROW('Zack');
