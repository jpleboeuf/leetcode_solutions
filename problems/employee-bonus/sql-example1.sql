CREATE TABLE IF NOT EXISTS Example1 (name VARCHAR(255), bonus INT);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (name, bonus) VALUES
  ROW('Brad', NULL),
  ROW('John', NULL),
  ROW('Dan',  500);
