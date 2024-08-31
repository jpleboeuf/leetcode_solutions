CREATE TABLE IF NOT EXISTS Example1 (name VARCHAR(255), population INT, area INT);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (name, population, area) VALUES
  ROW('Afghanistan', 25500100, 652230),
  ROW('Algeria', 37100000, 2381741);
